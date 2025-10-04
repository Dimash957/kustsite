# 🚀 Quick Start Guide

Get the AI Research Insights Platform running in **5 minutes**!

## Prerequisites

- Python 3.8+ installed
- Node.js 16+ installed
- Terminal/Command Prompt

## Step 1: Backend Setup (2 minutes)

Open a terminal and run:

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

✅ Backend should now be running at http://localhost:5000

**Note:** Without an OpenAI API key, the system uses mock data (perfect for testing!)

## Step 2: Frontend Setup (2 minutes)

Open a **NEW** terminal window and run:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start the app
npm start
```

✅ Frontend should auto-open at http://localhost:3000

## Step 3: Test It! (1 minute)

1. Copy this sample text:
```
This study examines accessibility barriers faced by visually impaired users 
when navigating e-commerce websites. Our findings reveal significant challenges 
including inadequate screen reader support, missing alternative text for product 
images, and complex navigation structures. Participants reported difficulty 
completing purchases independently, with 85% requiring assistance.
```

2. Paste into the text area
3. Keep defaults: "People with disabilities" and "Accessibility"
4. Click **"Analyze Text"**
5. 🎉 View the extracted challenges!

## Optional: Add OpenAI API Key

For real AI analysis (not required for testing):

1. Get API key from https://platform.openai.com
2. In `backend/` directory, create `.env` file:
```bash
OPENAI_API_KEY=sk-your-key-here
```
3. Restart backend server

## Troubleshooting

**"Port already in use"**
- Backend: Change port in `backend/app.py` line: `app.run(port=5001)`
- Frontend: Press `Y` when asked to use different port

**"Module not found"**
- Make sure virtual environment is activated
- Re-run `pip install -r requirements.txt`

**"npm errors"**
- Try: `npm install --legacy-peer-deps`

## Next Steps

- Read full documentation in `README.md`
- Try other sample texts from `examples/sample-research-text.md`
- Test accessibility with keyboard-only navigation (Tab key)
- Review code in `frontend/src/` and `backend/`

## Need Help?

- Check `SETUP.md` for detailed troubleshooting
- See `README.md` for full documentation
- Review `ACCESSIBILITY.md` for accessibility features

---

**That's it! You're ready to explore the platform! 🎉**
