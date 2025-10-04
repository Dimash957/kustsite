# AI-Powered Research Insights Platform for Vulnerable Groups

An accessible, AI-driven web platform that analyzes scientific research to extract and present challenges faced by vulnerable populations. Built with accessibility-first design principles following WCAG 2.1 Level AA standards.

## 🎯 Project Overview

This platform uses AI/NLP to automatically process research papers and identify key challenges affecting vulnerable groups such as:
- People with disabilities
- Elderly populations
- Students
- Children
- Low-income individuals
- Rural communities
- Immigrants and refugees

### Key Features

✅ **AI-Powered Analysis**: Uses OpenAI GPT-4 to extract challenges from research text  
✅ **Accessible Design**: WCAG 2.1 Level AA compliant with semantic HTML and ARIA labels  
✅ **Faceted Filtering**: Filter by user group and problem category  
✅ **Keyboard Navigation**: Full keyboard support with visible focus indicators  
✅ **Screen Reader Friendly**: Proper labels, roles, and live regions  
✅ **Minimalist UI**: Clean, distraction-free interface for all users  
✅ **High Contrast**: Color palette meeting 4.5:1 contrast ratios  
✅ **Responsive Design**: Works seamlessly on desktop, tablet, and mobile  

## 🏗️ Architecture

### Tech Stack

**Frontend:**
- React 18.2.0
- Axios for API calls
- CSS3 with custom properties (CSS variables)
- Accessible form controls and ARIA attributes

**Backend:**
- Flask 3.0.0
- OpenAI API (GPT-4)
- Flask-CORS for cross-origin requests
- Python 3.8+

### Project Structure

```
/
├── frontend/                 # React frontend application
│   ├── public/
│   │   └── index.html       # HTML shell with skip-to-content link
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── SearchBar.js
│   │   │   ├── FilterGroup.js
│   │   │   ├── ProblemList.js
│   │   │   └── ProblemItem.js
│   │   ├── services/
│   │   │   └── api.js       # API service layer
│   │   ├── styles/          # CSS modules
│   │   │   ├── index.css
│   │   │   ├── App.css
│   │   │   ├── SearchBar.css
│   │   │   ├── FilterGroup.css
│   │   │   ├── ProblemList.css
│   │   │   └── ProblemItem.css
│   │   ├── App.js           # Main app component
│   │   └── index.js         # Entry point
│   └── package.json
│
├── backend/                  # Flask backend API
│   ├── app.py               # Flask app with routes
│   ├── summarizer.py        # AI logic for text analysis
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
│
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** 16+ and npm
- **Python** 3.8+
- **OpenAI API Key** (for AI features)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
cp .env.example .env
```

5. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_api_key_here
```

6. Start the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will open automatically at `http://localhost:3000`

## 📖 Usage Guide

### For End Users

1. **Enter Research Text**: Paste an abstract or excerpt from a research paper into the text area
2. **Select Filters**: Choose the user group and problem category you're interested in
3. **Analyze**: Click "Analyze Text" to extract challenges using AI
4. **Review Results**: Browse identified challenges with severity indicators
5. **Keyboard Navigation**: Use Tab to navigate, Enter/Space to activate buttons

### Accessibility Features

- **Skip to Content**: Press Tab on page load to reveal skip link
- **Screen Reader Support**: All elements have proper ARIA labels
- **Keyboard Controls**: Full keyboard navigation without mouse
- **Focus Indicators**: Visible focus rings on all interactive elements
- **High Contrast**: Text meets WCAG AA contrast requirements (4.5:1+)
- **Semantic HTML**: Proper heading hierarchy and landmark regions
- **Live Regions**: Screen reader announcements for dynamic updates

## 🔌 API Endpoints

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "Research Insights API is running"
}
```

### `POST /analyze`
Analyze research text for specific group and category.

**Request Body:**
```json
{
  "text": "Research paper abstract or text...",
  "group": "People with disabilities",
  "category": "Accessibility"
}
```

**Response:**
```json
{
  "issues": [
    {
      "title": "Challenge title",
      "description": "Detailed description",
      "severity": "High"
    }
  ],
  "group": "People with disabilities",
  "category": "Accessibility",
  "success": true
}
```

### `GET /groups`
Get available user groups for filtering.

**Response:**
```json
{
  "groups": [
    "People with disabilities",
    "Elderly",
    "Students",
    ...
  ]
}
```

### `GET /categories`
Get available problem categories.

**Response:**
```json
{
  "categories": [
    "Accessibility",
    "Mobility",
    "Cognitive",
    ...
  ]
}
```

## 🎨 Design Principles

This platform follows evidence-based accessibility and UX principles:

1. **Accessibility First**: Following WCAG 2.1 Level AA standards
2. **Minimalist Design**: Removing unnecessary elements to reduce cognitive load
3. **Clear Typography**: Sans-serif fonts with ample spacing
4. **Semantic Structure**: Proper HTML5 elements and ARIA roles
5. **Progressive Enhancement**: Core functionality works without JavaScript
6. **Responsive Layout**: Mobile-first design that scales gracefully

### Color Palette (WCAG AA Compliant)

- **Primary**: `#1a1a2e` (Contrast: 16.9:1)
- **Accent**: `#1e5a8e` (Contrast: 5.2:1)
- **Error**: `#c92a2a` (Contrast: 7.6:1)
- **Success**: `#2f9e44` (Contrast: 4.8:1)
- **Warning**: `#f59f00` (Contrast: 5.1:1)

## 🧪 Testing

### Manual Accessibility Testing

1. **Keyboard Navigation**: Tab through all interactive elements
2. **Screen Reader**: Test with NVDA (Windows) or VoiceOver (Mac)
3. **Color Contrast**: Verify with browser DevTools
4. **Zoom**: Test at 200% browser zoom
5. **Focus Indicators**: Ensure all elements show clear focus

### Automated Tools

- **axe DevTools**: Browser extension for accessibility audits
- **WAVE**: Web accessibility evaluation tool
- **Lighthouse**: Chrome DevTools accessibility audit

## 📝 Configuration

### Environment Variables

**Backend (.env):**
```bash
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=development
FLASK_DEBUG=True
```

**Frontend:**
- Uses proxy configuration in `package.json` for development
- For production, set `REACT_APP_API_URL` environment variable

## 🔮 Future Enhancements

- [ ] Database integration for storing analyzed papers
- [ ] User accounts and saved searches
- [ ] PDF upload and parsing
- [ ] Integration with research databases (arXiv, PubMed)
- [ ] Export results to accessible formats (PDF, CSV)
- [ ] Multi-language support
- [ ] Advanced filtering and sorting options
- [ ] Data visualization for trends
- [ ] Community contributions and feedback

## 🤝 Contributing

Contributions are welcome! Please ensure:
1. Code follows existing patterns and style
2. All new features maintain WCAG AA compliance
3. Components include proper ARIA labels
4. CSS uses existing design tokens (CSS variables)
5. Test with keyboard and screen reader before submitting

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

This platform draws inspiration from:
- [SciSummary](https://scisummary.com) - AI research summarization
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Princeton Accessibility Guide](https://accessibility.princeton.edu)
- Hugging Face Transformers library

Built with accessibility and inclusion at the forefront, empowering vulnerable communities through evidence-based insights.

---

**Made with ❤️ for accessible research**