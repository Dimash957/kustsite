# API Documentation

This document describes the REST API endpoints for the AI Research Insights Platform.

## Base URL

```
http://localhost:5000
```

## Authentication

Currently, no authentication is required. In production, consider implementing API keys or OAuth.

## Endpoints

### Health Check

**GET** `/health`

Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "message": "AI Research Insights API is running"
}
```

### Analyze Research Text

**POST** `/analyze`

Analyze research text and extract issues for specific user groups.

**Request Body:**
```json
{
  "text": "Research paper text or abstract...",
  "user_group": "People with disabilities",
  "problem_category": "Accessibility"
}
```

**Response:**
```json
{
  "success": true,
  "issues": [
    {
      "id": 1,
      "title": "Digital Accessibility Barriers",
      "description": "Research shows that people with visual impairments face significant barriers...",
      "evidence": "Direct quote from the research text",
      "impact": "Description of impact on the target group",
      "confidence": 0.95,
      "user_group": "People with disabilities",
      "problem_category": "Accessibility",
      "source": "AI Analysis",
      "timestamp": "2024-01-01T00:00:00Z"
    }
  ],
  "metadata": {
    "user_group": "People with disabilities",
    "problem_category": "Accessibility",
    "total_issues": 1
  }
}
```

### Get Categories

**GET** `/categories`

Get available user groups and problem categories.

**Response:**
```json
{
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
}
```

### Search Issues

**POST** `/search`

Search through previously analyzed issues.

**Request Body:**
```json
{
  "query": "accessibility barriers",
  "filters": {
    "user_group": ["People with disabilities"],
    "problem_category": ["Accessibility", "Mobility"]
  }
}
```

**Response:**
```json
{
  "success": true,
  "results": [
    {
      "id": 1,
      "title": "Digital Accessibility Barriers",
      "description": "Research shows that people with visual impairments face significant barriers...",
      "user_group": "People with disabilities",
      "problem_category": "Accessibility",
      "source": "Journal of Accessibility Research, 2023",
      "confidence": 0.95
    }
  ],
  "total": 1
}
```

## Error Responses

All endpoints may return error responses in the following format:

```json
{
  "error": "Error message description"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `500` - Internal Server Error

## Rate Limiting

Currently no rate limiting is implemented. Consider implementing rate limiting in production.

## CORS

CORS is enabled for all origins in development. Configure appropriately for production.

## Example Usage

### Using curl

```bash
# Health check
curl http://localhost:5000/health

# Analyze text
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This study examines accessibility barriers in digital interfaces...",
    "user_group": "People with disabilities",
    "problem_category": "Accessibility"
  }'

# Get categories
curl http://localhost:5000/categories

# Search issues
curl -X POST http://localhost:5000/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "visual impairment",
    "filters": {
      "user_group": ["People with disabilities"],
      "problem_category": ["Accessibility"]
    }
  }'
```

### Using JavaScript (fetch)

```javascript
// Analyze text
const response = await fetch('http://localhost:5000/analyze', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Research text...',
    user_group: 'People with disabilities',
    problem_category: 'Accessibility'
  })
});

const data = await response.json();
console.log(data.issues);
```

## AI Model Configuration

The API uses OpenAI's GPT-4 model by default. To configure:

1. Set `OPENAI_API_KEY` environment variable
2. Modify `summarizer.py` to use different models
3. Adjust prompts in `_create_extraction_prompt()` method

## Future Enhancements

- **Authentication**: API key or OAuth integration
- **Rate Limiting**: Prevent abuse
- **Caching**: Cache analysis results
- **Batch Processing**: Analyze multiple texts at once
- **Webhooks**: Real-time notifications
- **Metrics**: Usage analytics and monitoring