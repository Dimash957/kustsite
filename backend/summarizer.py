from __future__ import annotations
import os
import re
from typing import List, Dict, Optional

OPENAI_API_KEY_ENV = "OPENAI_API_KEY"


def _split_bullets(text: str) -> List[str]:
    bullets = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        # Accept common bullet prefixes
        if re.match(r"^[-*•]\s+", stripped):
            bullets.append(re.sub(r"^[-*•]\s+", "", stripped))
        else:
            bullets.append(stripped)
    return bullets


def _heuristic_extract(text: str, group: Optional[str], category: Optional[str]) -> List[Dict]:
    # Very basic heuristic: grab sentences with keywords
    keywords = []
    if group:
        keywords.extend([w.strip().lower() for w in re.split(r"\W+", group) if w.strip()])
    if category:
        keywords.extend([w.strip().lower() for w in re.split(r"\W+", category) if w.strip()])

    # Add generic problem words
    keywords.extend([
        "barrier", "barriers", "challenge", "challenges", "limitation", "limitations",
        "difficulty", "difficulties", "access", "accessibility", "mobility", "impairment",
        "vision", "hearing", "cognitive", "mental", "health", "usability",
    ])

    # Split into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)
    matches = []
    for sent in sentences:
        sent_l = sent.lower()
        if any(k in sent_l for k in keywords):
            matches.append(sent.strip())

    if not matches and text:
        matches = [text.strip()[:280] + ("…" if len(text.strip()) > 280 else "")]  # fallback

    results = []
    for idx, s in enumerate(matches):
        results.append({
            "id": f"hx-{idx}",
            "summary": s,
            "quote": s,
            "group": group,
            "category": category,
            "source": "heuristic",
        })
    return results


def _openai_extract(text: str, group: Optional[str], category: Optional[str]) -> Optional[List[Dict]]:
    api_key = os.getenv(OPENAI_API_KEY_ENV)
    if not api_key:
        return None

    try:
        # Lazy import to avoid hard dependency if not configured
        import openai  # type: ignore
        openai.api_key = api_key

        prompt = (
            "You are an assistant that extracts research challenges.\n"
            f"Identify specific challenges faced by {group or 'the target group'} "
            f"related to {category or 'the stated domain'} from the text below.\n"
            "Return 5-10 bullet points, concise, plain language.\n"
            "For each bullet, include a short quote if present.\n"
            "Text:\n" + text
        )

        # Use Chat Completions if available
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # small fast model; can be adjusted
                messages=[
                    {"role": "system", "content": "Extract research challenges with quotes when possible."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
            )
            content = response["choices"][0]["message"]["content"].strip()
        except Exception:
            # Fallback to older completion API if needed
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=600,
                temperature=0.2,
            )
            content = response["choices"][0]["text"].strip()

        bullets = _split_bullets(content)
        results = []
        for idx, b in enumerate(bullets):
            # Try to pull a quote fragment within quotes
            m = re.search(r"[‘'\"]([^’'\"]{10,180})[’'\"]", b)
            quote = m.group(1).strip() if m else None
            results.append({
                "id": f"ai-{idx}",
                "summary": re.sub(r"\s+", " ", b).strip(),
                "quote": quote,
                "group": group,
                "category": category,
                "source": "openai",
            })
        return results or None
    except Exception:
        return None


def extract_issues(text: str, group: Optional[str], category: Optional[str]):
    """Attempt AI extraction, fallback to heuristic extraction.

    Returns a list of dicts: {id, summary, quote, group, category, source}
    """
    if not text or not text.strip():
        return []

    ai_results = _openai_extract(text, group, category)
    if ai_results:
        return ai_results
    return _heuristic_extract(text, group, category)
