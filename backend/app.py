from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import extract_issues, categorize_issues
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "AI Research Insights API is running"})

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze research text and extract issues for specific user groups
    Expected JSON payload:
    {
        "text": "research paper text or abstract",
        "user_group": "People with disabilities",
        "problem_category": "Accessibility"
    }
    """
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        text = data.get('text', '')
        user_group = data.get('user_group', 'People with disabilities')
        problem_category = data.get('problem_category', 'Accessibility')
        
        if not text.strip():
            return jsonify({"error": "No text provided for analysis"}), 400
        
        # Extract issues using AI
        issues = extract_issues(text, user_group, problem_category)
        
        # Categorize the issues
        categorized_issues = categorize_issues(issues, user_group, problem_category)
        
        return jsonify({
            "success": True,
            "issues": categorized_issues,
            "metadata": {
                "user_group": user_group,
                "problem_category": problem_category,
                "total_issues": len(categorized_issues)
            }
        })
        
    except Exception as e:
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500

@app.route('/categories', methods=['GET'])
def get_categories():
    """Get available user groups and problem categories"""
    return jsonify({
        "user_groups": [
            "People with disabilities",
            "Elderly",
            "Students",
            "Children",
            "Low-income individuals",
            "Rural populations",
            "Minority groups"
        ],
        "problem_categories": [
            "Accessibility",
            "Mobility",
            "Cognitive",
            "Mental health",
            "Education",
            "Employment",
            "Healthcare",
            "Technology",
            "Social inclusion",
            "Communication"
        ]
    })

@app.route('/search', methods=['POST'])
def search_issues():
    """
    Search through previously analyzed issues
    Expected JSON payload:
    {
        "query": "search terms",
        "filters": {
            "user_group": ["People with disabilities"],
            "problem_category": ["Accessibility", "Mobility"]
        }
    }
    """
    try:
        data = request.json
        query = data.get('query', '')
        filters = data.get('filters', {})
        
        # For now, return a mock response
        # In a real implementation, this would search a database
        mock_results = [
            {
                "id": 1,
                "title": "Digital Accessibility Barriers",
                "description": "Research shows that people with visual impairments face significant barriers when accessing digital content due to poor screen reader compatibility.",
                "user_group": "People with disabilities",
                "problem_category": "Accessibility",
                "source": "Journal of Accessibility Research, 2023",
                "confidence": 0.95
            },
            {
                "id": 2,
                "title": "Mobility Challenges in Public Transportation",
                "description": "Elderly individuals experience difficulties with public transportation systems that lack adequate accessibility features.",
                "user_group": "Elderly",
                "problem_category": "Mobility",
                "source": "Transportation Research, 2023",
                "confidence": 0.88
            }
        ]
        
        # Filter results based on query and filters
        filtered_results = []
        for result in mock_results:
            if query.lower() in result['title'].lower() or query.lower() in result['description'].lower():
                if not filters.get('user_group') or result['user_group'] in filters['user_group']:
                    if not filters.get('problem_category') or result['problem_category'] in filters['problem_category']:
                        filtered_results.append(result)
        
        return jsonify({
            "success": True,
            "results": filtered_results,
            "total": len(filtered_results)
        })
        
    except Exception as e:
        return jsonify({"error": f"Search failed: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)