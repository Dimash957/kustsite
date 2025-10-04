from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import extract_issues, analyze_paper
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Research Insights API is running"})

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze research text and extract issues for specific user groups.
    Expected JSON body:
    {
        "text": "research paper text or abstract",
        "group": "People with disabilities",
        "category": "Accessibility"
    }
    """
    try:
        data = request.json
        text = data.get('text', '')
        group = data.get('group', 'People with disabilities')
        category = data.get('category', 'Accessibility')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        # Extract issues using AI
        issues = extract_issues(text, group, category)
        
        return jsonify({
            "issues": issues,
            "group": group,
            "category": category,
            "success": True
        })
    
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500

@app.route('/analyze-paper', methods=['POST'])
def analyze_paper_endpoint():
    """
    Comprehensive paper analysis endpoint that extracts:
    - Key challenges
    - Affected user groups
    - Problem domains
    - Recommendations
    """
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        # Perform comprehensive analysis
        analysis = analyze_paper(text)
        
        return jsonify({
            "analysis": analysis,
            "success": True
        })
    
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500

@app.route('/groups', methods=['GET'])
def get_groups():
    """Get available user groups for filtering"""
    groups = [
        "People with disabilities",
        "Elderly",
        "Students",
        "Children",
        "Low-income individuals",
        "Rural communities",
        "Immigrants and refugees"
    ]
    return jsonify({"groups": groups})

@app.route('/categories', methods=['GET'])
def get_categories():
    """Get available problem categories for filtering"""
    categories = [
        "Accessibility",
        "Mobility",
        "Cognitive",
        "Mental health",
        "Education",
        "Healthcare",
        "Employment",
        "Housing",
        "Transportation",
        "Technology access"
    ]
    return jsonify({"categories": categories})

if __name__ == '__main__':
    # Check if API keys are configured
    if not os.getenv('OPENAI_API_KEY'):
        print("Warning: OPENAI_API_KEY not set. AI features will use mock data.")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
