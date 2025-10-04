# AI-Powered Research Insights Platform for Vulnerable Groups

A website that uses AI/NLP to read scientific literature and automatically extract key challenges faced by different user groups (starting with people with disabilities). The platform synthesizes research findings into an accessible knowledge base of issues.

## Features

- **AI/NLP Summarization**: Uses large language models to process research papers and identify relevant issues
- **Categorization by User Group**: Extracted issues are tagged by user type and problem area
- **Search and Filter UI**: Accessible search and filtering with faceted taxonomy
- **WCAG Compliance**: Highly accessible design following accessibility guidelines
- **Minimalist Design**: Clean, uncluttered interface for ease of use

## Tech Stack

- **Frontend**: React with accessible components
- **Backend**: Flask with AI/NLP processing
- **AI Models**: OpenAI API or Hugging Face transformers
- **Styling**: Minimalist CSS with high contrast

## Project Structure

```
/frontend          # React application
/backend           # Flask API server
/docs              # Documentation
```

## Getting Started

1. Install dependencies for both frontend and backend
2. Set up environment variables for AI API keys
3. Run the backend server
4. Run the frontend development server

## Accessibility

This platform follows WCAG 2.1 guidelines and Princeton's accessibility principles:
- High contrast text (4.5:1 minimum ratio)
- Clear typography with ample spacing
- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatibility