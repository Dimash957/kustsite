import os
import re
from typing import List, Dict, Any

# Try to import OpenAI, but gracefully handle if not available
try:
    import openai
    openai.api_key = os.getenv('OPENAI_API_KEY')
    OPENAI_AVAILABLE = bool(openai.api_key)
except ImportError:
    OPENAI_AVAILABLE = False
    print("OpenAI not available. Using mock summarization.")

def extract_issues(text: str, group: str, category: str) -> List[Dict[str, str]]:
    """
    Extract and summarize challenges from research text for a specific user group and category.
    
    Args:
        text: Research paper text or abstract
        group: Target user group (e.g., "People with disabilities")
        category: Problem category (e.g., "Accessibility")
    
    Returns:
        List of issue dictionaries with title, description, and severity
    """
    if OPENAI_AVAILABLE:
        return _extract_issues_with_ai(text, group, category)
    else:
        return _extract_issues_mock(text, group, category)

def _extract_issues_with_ai(text: str, group: str, category: str) -> List[Dict[str, str]]:
    """Use OpenAI API to extract issues"""
    try:
        prompt = f"""Analyze the following research text and extract specific challenges faced by {group} related to {category}.

For each challenge identified:
1. Provide a clear, concise title (5-10 words)
2. Write a brief description in plain language (2-3 sentences)
3. Assess severity as "High", "Medium", or "Low"

Format your response as a JSON array of objects with keys: title, description, severity

Research Text:
{text[:3000]}  # Limit text length for API

Respond ONLY with the JSON array, no other text."""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a research analyst specializing in accessibility and social issues. Extract key challenges in a clear, accessible format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        result = response['choices'][0]['message']['content']
        
        # Try to parse JSON response
        import json
        try:
            issues = json.loads(result)
            return issues if isinstance(issues, list) else []
        except json.JSONDecodeError:
            # Fallback: parse as text
            return _parse_text_response(result)
    
    except Exception as e:
        print(f"Error in AI extraction: {e}")
        return _extract_issues_mock(text, group, category)

def _parse_text_response(text: str) -> List[Dict[str, str]]:
    """Parse text response into structured issues"""
    issues = []
    # Simple parsing logic - look for bullet points or numbered items
    lines = text.split('\n')
    current_issue = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Look for titles (usually start with numbers, bullets, or are short)
        if re.match(r'^[\d\-\*•]', line) or (len(line) < 100 and ':' not in line):
            if current_issue:
                issues.append(current_issue)
            current_issue = {
                'title': re.sub(r'^[\d\-\*•\.\)]\s*', '', line),
                'description': '',
                'severity': 'Medium'
            }
        elif current_issue:
            current_issue['description'] += ' ' + line
    
    if current_issue:
        issues.append(current_issue)
    
    return issues

def _extract_issues_mock(text: str, group: str, category: str) -> List[Dict[str, str]]:
    """Mock extraction for demonstration when AI is not available"""
    # Extract key sentences that might indicate challenges
    sentences = text.split('.')
    relevant_sentences = []
    
    keywords = {
        'accessibility': ['barrier', 'difficult', 'challenge', 'limitation', 'access', 'unable', 'prevent'],
        'mobility': ['movement', 'transport', 'navigate', 'physical', 'walking', 'wheelchair'],
        'cognitive': ['understand', 'comprehend', 'learning', 'memory', 'attention', 'cognitive'],
        'mental health': ['stress', 'anxiety', 'depression', 'mental', 'psychological', 'emotional']
    }
    
    category_keywords = keywords.get(category.lower(), ['challenge', 'issue', 'problem', 'difficulty'])
    
    for sentence in sentences[:20]:  # Limit to first 20 sentences
        sentence_lower = sentence.lower()
        if any(keyword in sentence_lower for keyword in category_keywords):
            relevant_sentences.append(sentence.strip())
    
    # Create mock issues
    issues = []
    for i, sentence in enumerate(relevant_sentences[:5]):  # Max 5 issues
        issues.append({
            'title': f"{category} Challenge {i+1} for {group}",
            'description': sentence if sentence else f"A {category.lower()} challenge affecting {group.lower()} identified in the research.",
            'severity': ['High', 'Medium', 'Low'][i % 3],
            'source': 'extractive'
        })
    
    # Add at least one issue if none found
    if not issues:
        issues.append({
            'title': f"Research on {category} and {group}",
            'description': f"This research discusses aspects of {category.lower()} relevant to {group.lower()}. More detailed analysis requires full text processing.",
            'severity': 'Medium',
            'source': 'summary'
        })
    
    return issues

def analyze_paper(text: str) -> Dict[str, Any]:
    """
    Comprehensive paper analysis that identifies:
    - Multiple user groups affected
    - Multiple problem domains
    - Key challenges
    - Recommendations
    """
    if OPENAI_AVAILABLE:
        return _analyze_paper_with_ai(text)
    else:
        return _analyze_paper_mock(text)

def _analyze_paper_with_ai(text: str) -> Dict[str, Any]:
    """Use AI for comprehensive paper analysis"""
    try:
        prompt = f"""Analyze this research paper and provide a comprehensive summary in JSON format:

1. user_groups: List of user groups discussed (e.g., ["elderly", "people with disabilities"])
2. problem_domains: List of problem areas (e.g., ["accessibility", "mobility"])
3. key_challenges: Array of 3-5 main challenges, each with title and description
4. recommendations: Array of 2-3 actionable recommendations

Research Text:
{text[:4000]}

Respond with ONLY a JSON object."""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a research analyst. Provide structured JSON analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500
        )
        
        result = response['choices'][0]['message']['content']
        import json
        return json.loads(result)
    
    except Exception as e:
        print(f"Error in AI analysis: {e}")
        return _analyze_paper_mock(text)

def _analyze_paper_mock(text: str) -> Dict[str, Any]:
    """Mock comprehensive analysis"""
    return {
        'user_groups': ['People with disabilities', 'Elderly'],
        'problem_domains': ['Accessibility', 'Technology access'],
        'key_challenges': [
            {
                'title': 'Digital accessibility barriers',
                'description': 'Many digital platforms lack proper accessibility features for users with disabilities.'
            },
            {
                'title': 'Limited technology literacy',
                'description': 'Older adults face challenges in adopting new technologies due to limited training resources.'
            }
        ],
        'recommendations': [
            'Implement WCAG 2.1 standards for all digital platforms',
            'Provide accessible training programs for vulnerable populations'
        ]
    }
