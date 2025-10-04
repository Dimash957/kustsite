# Research Insights Backend API

Flask-based REST API with AI-powered research text analysis.

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# Run server
python app.py
```

Server runs on `http://localhost:5000`

## API Endpoints

### Health Check

**GET** `/health`

Check if API is running.

```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "Research Insights API is running"
}
```

---

### Analyze Text

**POST** `/analyze`

Extract challenges from research text for specific user group and category.

**Request:**
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Research shows that elderly users face significant challenges with small touchscreen buttons and complex navigation...",
    "group": "Elderly",
    "category": "Technology access"
  }'
```

**Parameters:**
- `text` (required): Research paper text or abstract
- `group` (required): Target user group
- `category` (required): Problem category

**Response:**
```json
{
  "issues": [
    {
      "title": "Small touchscreen controls",
      "description": "Elderly users struggle with small buttons that are difficult to press accurately.",
      "severity": "High"
    }
  ],
  "group": "Elderly",
  "category": "Technology access",
  "success": true
}
```

---

### Get User Groups

**GET** `/groups`

Retrieve available user groups for filtering.

```bash
curl http://localhost:5000/groups
```

**Response:**
```json
{
  "groups": [
    "People with disabilities",
    "Elderly",
    "Students",
    "Children",
    "Low-income individuals",
    "Rural communities",
    "Immigrants and refugees"
  ]
}
```

---

### Get Categories

**GET** `/categories`

Retrieve available problem categories.

```bash
curl http://localhost:5000/categories
```

**Response:**
```json
{
  "categories": [
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
}
```

---

### Analyze Paper (Comprehensive)

**POST** `/analyze-paper`

Comprehensive analysis identifying multiple groups, domains, and recommendations.

**Request:**
```bash
curl -X POST http://localhost:5000/analyze-paper \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Full research paper text..."
  }'
```

**Response:**
```json
{
  "analysis": {
    "user_groups": ["Elderly", "People with disabilities"],
    "problem_domains": ["Accessibility", "Technology access"],
    "key_challenges": [
      {
        "title": "Digital accessibility barriers",
        "description": "Many platforms lack proper accessibility features."
      }
    ],
    "recommendations": [
      "Implement WCAG 2.1 standards",
      "Provide accessible training programs"
    ]
  },
  "success": true
}
```

## Architecture

### app.py
Flask application with route definitions and error handling.

**Features:**
- CORS enabled for frontend communication
- JSON request/response handling
- Error handling with appropriate status codes
- Environment variable configuration

### summarizer.py
AI logic for text analysis and challenge extraction.

**Features:**
- OpenAI GPT-4 integration
- Fallback to mock data when API unavailable
- Extractive and abstractive summarization
- Structured JSON output

**Functions:**
- `extract_issues(text, group, category)` - Extract specific issues
- `analyze_paper(text)` - Comprehensive paper analysis
- `_extract_issues_with_ai()` - AI-powered extraction
- `_extract_issues_mock()` - Mock extraction for testing

## Configuration

### Environment Variables

Create a `.env` file:

```bash
OPENAI_API_KEY=sk-your-api-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

### OpenAI API

The backend uses OpenAI's GPT-4 model for text analysis.

**Without API Key:**
- System uses mock data for testing
- Warning message displayed on startup
- Functional for development without costs

**With API Key:**
- Real AI-powered analysis
- More accurate issue extraction
- Costs per API call (see OpenAI pricing)

### Model Configuration

Default model: `gpt-4`

To change the model, edit `summarizer.py`:

```python
response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[...],
    temperature=0.3,
    max_tokens=1000
)
```

## Error Handling

### Common Errors

**400 Bad Request**
```json
{
  "error": "No text provided",
  "success": false
}
```

**500 Internal Server Error**
```json
{
  "error": "Error message details",
  "success": false
}
```

## Testing

### Manual Testing

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test analysis with sample text
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d @test_data.json
```

### Python Testing

Create `test_app.py`:

```python
import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
    
    def test_analyze(self):
        data = {
            'text': 'Sample research text...',
            'group': 'Elderly',
            'category': 'Accessibility'
        }
        response = self.client.post('/analyze', json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
python test_app.py
```

## Dependencies

- **Flask** (3.0.0) - Web framework
- **flask-cors** (4.0.0) - Cross-origin resource sharing
- **openai** (1.3.0) - OpenAI API client
- **python-dotenv** (1.0.0) - Environment variable management
- **requests** (2.31.0) - HTTP library

Install all:
```bash
pip install -r requirements.txt
```

## Deployment

### Development

```bash
python app.py
```

Runs with Flask development server on `http://0.0.0.0:5000`

### Production

Use a production WSGI server like Gunicorn:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t research-insights-api .
docker run -p 5000:5000 --env-file .env research-insights-api
```

## Performance

### Response Times

- Health check: ~10ms
- Groups/Categories: ~20ms
- Analysis (mock): ~100ms
- Analysis (GPT-4): ~2-5 seconds

### Rate Limiting

OpenAI has rate limits:
- Free tier: 3 requests/minute
- Paid tier: Varies by plan

Consider implementing request caching or rate limiting for production.

### Caching

To reduce API calls, implement caching:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def extract_issues_cached(text, group, category):
    return extract_issues(text, group, category)
```

## Security

### API Key Protection

- Never commit `.env` file to git
- Use environment variables in production
- Rotate API keys regularly

### CORS Configuration

Production CORS should be restricted:

```python
CORS(app, origins=['https://your-frontend-domain.com'])
```

### Input Validation

Current validation:
- Text length limits (3000-4000 characters)
- Required fields check
- JSON format validation

## Troubleshooting

### "ModuleNotFoundError"
Activate virtual environment and install dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### "OpenAI API Error"
Check:
- API key is correct in `.env`
- API key has credits
- Internet connection is working

### "Port already in use"
Change port in `app.py`:
```python
app.run(port=5001)
```

### "CORS errors"
Ensure flask-cors is installed and configured correctly.

## Contributing

When adding new endpoints:

1. Add route to `app.py`
2. Implement logic in appropriate module
3. Add error handling
4. Update this README
5. Test with curl or Postman
6. Update frontend API service if needed

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

---

**Built with Flask and OpenAI for accessible research insights**
