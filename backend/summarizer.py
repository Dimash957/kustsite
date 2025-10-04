import openai
import os
import re
from typing import List, Dict, Any
import json

class AIResearchSummarizer:
    """
    AI-powered summarizer for extracting research insights relevant to vulnerable groups
    """
    
    def __init__(self):
        # Initialize OpenAI client
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.model = "gpt-4"
    
    def extract_issues(self, text: str, user_group: str, problem_category: str) -> List[Dict[str, Any]]:
        """
        Extract relevant issues from research text for a specific user group and problem category
        """
        try:
            prompt = self._create_extraction_prompt(text, user_group, problem_category)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert research analyst specializing in identifying challenges faced by vulnerable populations in scientific literature. Extract specific, actionable issues with clear evidence from the text."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1500
            )
            
            result = response.choices[0].message.content
            return self._parse_extraction_result(result)
            
        except Exception as e:
            print(f"Error in AI extraction: {e}")
            return self._fallback_extraction(text, user_group, problem_category)
    
    def _create_extraction_prompt(self, text: str, user_group: str, problem_category: str) -> str:
        """Create a structured prompt for issue extraction"""
        return f"""
Analyze the following research text and identify specific challenges, barriers, or problems faced by {user_group} related to {problem_category}.

Research Text:
{text[:3000]}  # Limit text length for API efficiency

Instructions:
1. Focus specifically on issues affecting {user_group}
2. Look for problems related to {problem_category}
3. Extract concrete, specific challenges rather than general statements
4. Include relevant quotes or evidence from the text
5. Format each issue as a structured item with:
   - Title: Brief descriptive title
   - Description: Detailed explanation of the challenge
   - Evidence: Direct quote or reference from the text
   - Impact: How this affects the target group

Return the results as a JSON array of objects with the following structure:
[
  {{
    "title": "Issue title",
    "description": "Detailed description of the challenge",
    "evidence": "Direct quote or reference from the text",
    "impact": "Description of impact on the target group",
    "confidence": 0.85
  }}
]

If no relevant issues are found, return an empty array [].
"""
    
    def _parse_extraction_result(self, result: str) -> List[Dict[str, Any]]:
        """Parse the AI response into structured data"""
        try:
            # Try to extract JSON from the response
            json_match = re.search(r'\[.*\]', result, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                return json.loads(json_str)
            else:
                # Fallback: parse as text and structure
                return self._parse_text_result(result)
        except json.JSONDecodeError:
            return self._parse_text_result(result)
    
    def _parse_text_result(self, result: str) -> List[Dict[str, Any]]:
        """Parse text-based result into structured format"""
        issues = []
        lines = result.split('\n')
        current_issue = {}
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('Title:') or line.startswith('Issue:'):
                if current_issue:
                    issues.append(current_issue)
                current_issue = {
                    'title': line.split(':', 1)[1].strip(),
                    'description': '',
                    'evidence': '',
                    'impact': '',
                    'confidence': 0.8
                }
            elif line.startswith('Description:'):
                current_issue['description'] = line.split(':', 1)[1].strip()
            elif line.startswith('Evidence:'):
                current_issue['evidence'] = line.split(':', 1)[1].strip()
            elif line.startswith('Impact:'):
                current_issue['impact'] = line.split(':', 1)[1].strip()
        
        if current_issue:
            issues.append(current_issue)
        
        return issues
    
    def _fallback_extraction(self, text: str, user_group: str, problem_category: str) -> List[Dict[str, Any]]:
        """Fallback extraction method when AI fails"""
        # Simple keyword-based extraction as fallback
        keywords = {
            'accessibility': ['barrier', 'accessible', 'accommodation', 'assistive'],
            'mobility': ['mobility', 'movement', 'transportation', 'navigation'],
            'cognitive': ['cognitive', 'memory', 'learning', 'understanding'],
            'mental health': ['mental health', 'depression', 'anxiety', 'stress'],
            'education': ['education', 'learning', 'school', 'academic'],
            'employment': ['employment', 'work', 'job', 'career'],
            'healthcare': ['healthcare', 'medical', 'treatment', 'health'],
            'technology': ['technology', 'digital', 'software', 'device'],
            'social inclusion': ['social', 'isolation', 'community', 'inclusion'],
            'communication': ['communication', 'language', 'speech', 'interaction']
        }
        
        relevant_keywords = keywords.get(problem_category.lower(), [])
        found_issues = []
        
        # Simple text analysis
        sentences = text.split('.')
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in relevant_keywords):
                if user_group.lower() in sentence.lower() or 'disability' in sentence.lower():
                    found_issues.append({
                        'title': f"{problem_category} Challenge",
                        'description': sentence.strip(),
                        'evidence': sentence.strip(),
                        'impact': f"Affects {user_group}",
                        'confidence': 0.6
                    })
        
        return found_issues[:5]  # Limit to 5 issues

# Global instance
summarizer = AIResearchSummarizer()

def extract_issues(text: str, user_group: str, problem_category: str) -> List[Dict[str, Any]]:
    """Main function to extract issues from research text"""
    return summarizer.extract_issues(text, user_group, problem_category)

def categorize_issues(issues: List[Dict[str, Any]], user_group: str, problem_category: str) -> List[Dict[str, Any]]:
    """Add categorization metadata to extracted issues"""
    categorized = []
    for i, issue in enumerate(issues):
        categorized_issue = {
            **issue,
            'id': i + 1,
            'user_group': user_group,
            'problem_category': problem_category,
            'source': 'AI Analysis',
            'timestamp': '2024-01-01T00:00:00Z'
        }
        categorized.append(categorized_issue)
    
    return categorized