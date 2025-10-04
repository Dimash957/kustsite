import json
import os
import re
from typing import List, Dict, Any, Optional


KEYWORDS = [
    "challenge", "barrier", "difficulty", "problem", "issue", "limitation",
    "impair", "access", "inaccessible", "usability", "mobility", "accommodation",
    "support need", "constraint", "risk", "burden", "inequity", "inequality",
    "disparity", "fatigue", "pain", "stigma", "bias"
]

SENTENCE_SPLIT_REGEX = re.compile(r"(?<=[.!?])\s+")


def _rule_based_issues(text: str, group: Optional[str], category: Optional[str]) -> List[Dict[str, Any]]:
    sentences = re.split(SENTENCE_SPLIT_REGEX, text.strip())
    issues: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for sentence in sentences:
        lowered = sentence.lower()
        if any(k in lowered for k in KEYWORDS):
            # Use a normalized key to deduplicate similar sentences
            key = lowered[:200]
            if key in seen:
                continue
            seen.add(key)
            title = sentence.strip()
            if len(title) > 120:
                title = title[:117].rstrip() + "..."
            issues.append({
                "title": title,
                "description": sentence.strip(),
                "group": group,
                "categories": [category] if isinstance(category, str) and category else (category or [])
            })
    # Provide at least one generic item if nothing matched
    if not issues and text.strip():
        preview = text.strip().splitlines()[0]
        if len(preview) > 120:
            preview = preview[:117].rstrip() + "..."
        issues.append({
            "title": "Potential challenges mentioned in the text",
            "description": preview,
            "group": group,
            "categories": [category] if isinstance(category, str) and category else (category or [])
        })
    return issues


def _openai_issues(text: str, group: Optional[str], category: Optional[str]) -> Optional[List[Dict[str, Any]]]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
        system = (
            "You are an assistant that extracts research challenges affecting specific user groups. "
            "Return only valid JSON with a top-level key 'issues', where each issue has: 'title', 'description'."
        )
        user = (
            "Extract distinct challenges faced by the specified user group related to the given category.\n"
            f"User group: {group or 'unspecified'}\n"
            f"Category: {category or 'unspecified'}\n\n"
            "Return 3-8 succinct issues based on the text.\n"
            "Text to analyze: " + text
        )
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
        )
        content = resp.choices[0].message.content
        data = json.loads(content)
        raw_issues = data.get("issues")
        if not isinstance(raw_issues, list):
            return None
        issues: List[Dict[str, Any]] = []
        for item in raw_issues:
            title = str(item.get("title", "")).strip()
            description = str(item.get("description", "")).strip()
            if not title:
                continue
            issues.append({
                "title": title,
                "description": description or title,
                "group": group,
                "categories": [category] if isinstance(category, str) and category else (category or [])
            })
        return issues or None
    except Exception:
        # Any failure (import/network/parse) -> None to allow fallback
        return None


def extract_issues(text: str, group: Optional[str] = None, category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Best-effort pipeline:
    1) If OpenAI API available, request structured JSON issues.
    2) Fallback to lightweight rule-based extraction using keywords.
    """
    # 1) Try OpenAI if configured
    issues = _openai_issues(text=text, group=group, category=category)
    if issues:
        return issues

    # 2) Rule-based fallback
    return _rule_based_issues(text=text, group=group, category=category)
