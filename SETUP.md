# Quick Setup Guide

This guide will help you get the Research Insights Platform up and running in minutes.

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Node.js 16 or higher installed (`node --version`)
- [ ] Python 3.8 or higher installed (`python --version`)
- [ ] npm installed (`npm --version`)
- [ ] Git installed (for cloning the repository)
- [ ] OpenAI API key (sign up at https://platform.openai.com)

## Quick Start (5 Minutes)

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd research-insights-platform
```

### 2. Backend Setup (2 minutes)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here

# Start the server
python app.py
```

The backend should now be running at `http://localhost:5000`

### 3. Frontend Setup (2 minutes)

Open a new terminal window:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will automatically open at `http://localhost:3000`

## Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

**Problem**: `Warning: OPENAI_API_KEY not set`
- **Solution**: This is okay for testing! The app will use mock data. To use real AI, add your OpenAI API key to `.env`

**Problem**: Port 5000 already in use
- **Solution**: Stop any other Flask apps or change the port in `app.py`: `app.run(port=5001)`

### Frontend Issues

**Problem**: `npm ERR! network` errors
- **Solution**: Try using `npm install --legacy-peer-deps`

**Problem**: Port 3000 already in use
- **Solution**: The terminal will ask if you want to use a different port (usually 3001). Press `Y`

**Problem**: Can't connect to backend
- **Solution**: Ensure the backend is running on port 5000. Check `http://localhost:5000/health`

## Testing the Application

1. **Open the frontend**: Navigate to `http://localhost:3000`

2. **Test with sample text**: Copy this sample research abstract:

```
This study examines accessibility barriers faced by visually impaired users 
when navigating e-commerce websites. Our findings reveal significant challenges 
including inadequate screen reader support, missing alternative text for product 
images, and complex navigation structures. Participants reported difficulty 
completing purchases independently, with 85% requiring assistance. The research 
highlights the urgent need for WCAG 2.1 compliance and user testing with people 
with disabilities during website development.
```

3. **Paste and analyze**:
   - Paste the text into the search box
   - Select "People with disabilities" for User Group
   - Select "Accessibility" for Problem Category
   - Click "Analyze Text"

4. **View results**: You should see AI-extracted challenges with severity indicators

## Keyboard Navigation Test

To test accessibility:

1. Press `Tab` after page loads → Should show "Skip to content" link
2. Press `Tab` again → Should focus on the textarea
3. Type/paste text, then `Tab` to "Analyze Text" button
4. Press `Enter` or `Space` to submit
5. Use `Tab` to navigate through filters and results
6. All focus states should be clearly visible

## Next Steps

### For Development

- Read the full documentation in `README.md`
- Explore the code structure in `/frontend/src` and `/backend`
- Modify filters in `app.py` (backend) and `App.js` (frontend)
- Customize styling in `/frontend/src/styles`

### For Testing

- Test with a screen reader:
  - Windows: NVDA (free, open source)
  - Mac: VoiceOver (built-in, press Cmd+F5)
  - Chrome: ChromeVox extension
- Test keyboard-only navigation (no mouse)
- Test at 200% browser zoom
- Run Lighthouse accessibility audit in Chrome DevTools

### For Production

1. Get a production OpenAI API key
2. Set environment variables for production
3. Build the frontend: `npm run build`
4. Deploy backend with a WSGI server (e.g., Gunicorn)
5. Set up HTTPS for secure API calls
6. Configure CORS for your production domain

## Getting Help

- Check `README.md` for detailed documentation
- Review component code for implementation examples
- Open an issue on GitHub for bugs or questions
- Consult WCAG guidelines for accessibility questions

## Quick Reference

### Common Commands

**Backend:**
```bash
python app.py                 # Start server
pip install <package>         # Install new package
pip freeze > requirements.txt # Update dependencies
```

**Frontend:**
```bash
npm start                     # Development server
npm run build                # Production build
npm test                     # Run tests
```

### Important URLs

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000`
- API Health Check: `http://localhost:5000/health`
- API Docs: See README.md

### File Locations

- Backend config: `backend/.env`
- Frontend config: `frontend/package.json`
- API endpoints: `backend/app.py`
- AI logic: `backend/summarizer.py`
- Main React app: `frontend/src/App.js`
- Styles: `frontend/src/styles/`

---

**Happy coding! 🚀**
