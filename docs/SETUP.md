# Setup Guide

This guide will help you set up and run the AI Research Insights Platform for Vulnerable Groups.

## Prerequisites

- **Python 3.8+** for the backend
- **Node.js 16+** and **npm** for the frontend
- **OpenAI API Key** for AI processing

## Quick Start

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd /workspace

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install
```

### 2. Environment Configuration

Create a `.env` file in the backend directory:

```bash
cd backend
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
FLASK_ENV=development
PORT=5000
```

### 3. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Detailed Setup

### Backend Setup

1. **Create Virtual Environment (Recommended):**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Environment Variables:**
```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
FLASK_ENV=development
PORT=5000
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

4. **Run the Server:**
```bash
python app.py
```

### Frontend Setup

1. **Install Dependencies:**
```bash
cd frontend
npm install
```

2. **Environment Variables (Optional):**
Create `.env` file in frontend directory:
```env
REACT_APP_API_URL=http://localhost:5000
```

3. **Run Development Server:**
```bash
npm start
```

## Configuration Options

### Backend Configuration

**Flask Settings:**
- `FLASK_ENV`: Set to `development` for debug mode
- `PORT`: Server port (default: 5000)

**AI Model Settings:**
- `OPENAI_API_KEY`: Required for GPT-4 analysis
- `HUGGINGFACE_API_KEY`: Optional for alternative models

**CORS Settings:**
- Currently allows all origins in development
- Configure for production deployment

### Frontend Configuration

**API URL:**
- Default: `http://localhost:5000`
- Set via `REACT_APP_API_URL` environment variable

**Build Settings:**
- `npm run build`: Creates production build
- `npm test`: Runs test suite

## Production Deployment

### Backend Deployment

1. **Environment Setup:**
```bash
export FLASK_ENV=production
export OPENAI_API_KEY=your_production_key
```

2. **WSGI Server:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend Deployment

1. **Build Production Version:**
```bash
npm run build
```

2. **Serve Static Files:**
Use nginx, Apache, or a CDN to serve the `build` directory.

### Docker Deployment

**Backend Dockerfile:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Frontend Dockerfile:**
```dockerfile
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## Troubleshooting

### Common Issues

**1. OpenAI API Key Error:**
```
Error: No API key provided
```
Solution: Ensure `OPENAI_API_KEY` is set in your `.env` file.

**2. CORS Error:**
```
Access to fetch at 'http://localhost:5000' from origin 'http://localhost:3000' has been blocked by CORS policy
```
Solution: Ensure the backend is running and CORS is enabled.

**3. Module Not Found:**
```
ModuleNotFoundError: No module named 'flask'
```
Solution: Install requirements: `pip install -r requirements.txt`

**4. Port Already in Use:**
```
OSError: [Errno 98] Address already in use
```
Solution: Change the port in `.env` or kill the process using the port.

### Performance Optimization

**Backend:**
- Use a production WSGI server (gunicorn)
- Implement caching for repeated analyses
- Add rate limiting for API endpoints

**Frontend:**
- Enable gzip compression
- Use a CDN for static assets
- Implement service worker for offline support

### Security Considerations

**Production Checklist:**
- [ ] Set strong API keys
- [ ] Enable HTTPS
- [ ] Configure CORS properly
- [ ] Add rate limiting
- [ ] Implement input validation
- [ ] Use environment variables for secrets
- [ ] Regular security updates

## Development

### Adding New Features

1. **Backend:** Add new endpoints in `app.py`
2. **Frontend:** Create components in `src/components/`
3. **Styling:** Update `src/styles/App.css`
4. **Testing:** Add tests in respective test directories

### Code Style

- **Python:** Follow PEP 8
- **JavaScript:** Use ESLint configuration
- **CSS:** Follow BEM methodology for class names

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Check accessibility guidelines
4. Create an issue in the project repository