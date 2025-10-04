# AI-Powered Research Insights Platform for Vulnerable Groups

## Project Overview

This platform uses AI/NLP to read scientific literature and automatically extract key challenges faced by different user groups, starting with people with disabilities. The purpose is to synthesize research findings into an accessible knowledge base of issues.

## Key Features

### 🤖 AI/NLP Summarization
- Uses OpenAI GPT-4 to process research papers
- Extracts relevant issues for specific user groups
- Provides both extractive (quotes) and abstractive (summaries) results
- Confidence scoring for each extracted issue

### 🏷️ Categorization System
- **User Groups**: People with disabilities, Elderly, Students, Children, Low-income individuals, Rural populations, Minority groups
- **Problem Categories**: Accessibility, Mobility, Cognitive, Mental health, Education, Employment, Healthcare, Technology, Social inclusion, Communication
- Faceted taxonomy allowing multi-dimensional filtering

### 🔍 Search and Filter UI
- Accessible search interface with clear labels
- Radio button filters with proper ARIA attributes
- Real-time search through analyzed issues
- Keyboard navigation support

### ♿ WCAG Compliance
- High contrast design (4.5:1 minimum ratio)
- Semantic HTML structure with proper headings
- ARIA labels and roles for screen readers
- Keyboard-only navigation support
- Focus management and live regions

### 🎨 Minimalist Design
- Clean, uncluttered interface
- High contrast colors for readability
- Sans-serif typography with ample spacing
- Responsive design for all devices

## Technical Architecture

### Backend (Flask + Python)
```
/backend
├── app.py              # Flask API server
├── summarizer.py       # AI/NLP processing logic
├── requirements.txt    # Python dependencies
└── .env.example       # Environment configuration
```

**Key Endpoints:**
- `POST /analyze` - Analyze research text
- `GET /categories` - Get user groups and categories
- `POST /search` - Search through issues
- `GET /health` - Health check

### Frontend (React + JavaScript)
```
/frontend
├── src/
│   ├── components/     # Accessible React components
│   ├── services/       # API integration
│   └── styles/         # WCAG-compliant CSS
├── public/             # Static assets
└── package.json        # Dependencies
```

**Key Components:**
- `SearchBar` - Accessible search input
- `FilterGroup` - Radio button filters with ARIA
- `ProblemList` - Results display with semantic structure
- `ProblemItem` - Individual issue cards

## Accessibility Features

### WCAG 2.1 AA Compliance
- **Perceivable**: High contrast, text alternatives, resizable text
- **Operable**: Keyboard navigation, no seizures, consistent navigation
- **Understandable**: Clear language, predictable behavior, input assistance
- **Robust**: Compatible with assistive technologies, valid HTML

### Implementation Details
- Semantic HTML with proper roles and landmarks
- ARIA labels, descriptions, and live regions
- Focus management and keyboard shortcuts
- Screen reader compatibility
- High contrast and reduced motion support

## Getting Started

### Quick Setup
```bash
# Backend
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your OpenAI API key
python app.py

# Frontend (new terminal)
cd frontend
npm install
npm start
```

### Test Setup
```bash
python test_setup.py
```

## Usage Examples

### Analyzing Research Text
1. Select user group (e.g., "People with disabilities")
2. Select problem category (e.g., "Accessibility")
3. Paste research text or abstract
4. Click "Analyze Text"
5. Review extracted issues with confidence scores

### Searching Issues
1. Switch to "Search Issues" tab
2. Enter search terms
3. Apply filters for user group and category
4. Browse results with expandable details

## AI Processing

### Prompt Engineering
The system uses carefully crafted prompts to:
- Focus on specific user groups and problem categories
- Extract concrete, actionable challenges
- Provide evidence from the source text
- Assess confidence levels for each finding

### Example Prompt Structure
```
Analyze the following research text and identify specific challenges, 
barriers, or problems faced by {user_group} related to {problem_category}.

Instructions:
1. Focus specifically on issues affecting {user_group}
2. Look for problems related to {problem_category}
3. Extract concrete, specific challenges rather than general statements
4. Include relevant quotes or evidence from the text
```

## Future Enhancements

### Planned Features
- **Database Integration**: Store and search through analyzed issues
- **Batch Processing**: Analyze multiple papers at once
- **Export Functionality**: Download results in various formats
- **User Accounts**: Save and manage analysis history
- **Advanced Filters**: Date ranges, source types, confidence levels

### Technical Improvements
- **Caching**: Cache analysis results for performance
- **Rate Limiting**: Prevent API abuse
- **Monitoring**: Usage analytics and error tracking
- **Security**: Authentication and authorization
- **Scalability**: Microservices architecture

## Contributing

### Development Guidelines
- Follow accessibility best practices
- Maintain WCAG compliance
- Use semantic HTML and ARIA attributes
- Test with screen readers and keyboard navigation
- Ensure high contrast and readability

### Code Style
- **Python**: PEP 8 compliance
- **JavaScript**: ESLint configuration
- **CSS**: BEM methodology for class names
- **Accessibility**: ARIA-first approach

## License

This project is designed to empower vulnerable communities by making research insights accessible. The platform follows open-source principles and accessibility standards to ensure inclusive access to scientific knowledge.

## Support

For technical support or accessibility questions:
1. Check the documentation in `/docs`
2. Run the setup test: `python test_setup.py`
3. Review accessibility guidelines in `docs/ACCESSIBILITY.md`
4. Test with assistive technologies

---

*This platform demonstrates how AI can be used ethically to serve vulnerable populations by making complex research accessible and actionable.*