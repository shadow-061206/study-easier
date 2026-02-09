# 📚 AI Study Assistant Chatbot

An intelligent AI-powered study companion built with Streamlit and Python. Perfect for students who want personalized learning support.

## Features ✨

- **Multiple Study Modes**: Chat, Q&A, Quiz, and Flashcards
- **Real-time AI Responses**: Powered by Google's Gemini API
- **Conversation History**: Keep track of all your questions and answers
- **Study Tips**: Get daily study motivation and tips
- **Clean UI**: Modern, intuitive interface designed for learning
- **Secure**: Your API key is kept private and never stored

## Prerequisites 📋

- Python
- Streamlit
- A free Google Gemini API Key (from https://makersuite.google.com/app/apikey)

## Installation 🚀

1. **Clone or download this project**
# Study Easier — AI Study Assistant

Lightweight Streamlit app that helps students learn with AI-powered Chat, Q&A, Quiz, and Flashcards modes.

Key points:
- Fast local UI using Streamlit
- Uses Google's Gemini (via `google-generativeai`) by default
- Supports uploading notes (PDF/TXT) to provide context

Files:
- [ai_study.py](ai_study.py)
- [requirements.txt](requirements.txt)

Prerequisites
- Python 3.8+
- See `requirements.txt` for Python dependencies (`streamlit`, `google-generativeai`)

Install
1. Clone or download the repository.
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Configuration (API Key)
The app requires an API key for the AI provider. Do NOT commit API keys into the source.

Recommended: set an environment variable before running:
```powershell
setx GOOGLE_API_KEY "your_api_key_here"
# then restart your terminal/session
```

If you prefer to inject the key directly (not recommended), open [ai_study.py](ai_study.py) and replace the placeholder. Better: change this line to read from the environment:
```python
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

Run
```bash
streamlit run ai_study.py
```
Open http://localhost:8501 in your browser if Streamlit doesn't open it automatically.

Usage
- Enter a student name in the sidebar.
- Choose a Study Mode: Chat, Q&A, Quiz, or Flashcards.
- (Optional) Upload PDF or TXT notes in the sidebar to provide context.
- Type a topic/question in the chat input and submit.

Security & privacy
- Never commit API keys to source control.
- If using local models (for full privacy), adapt the code to use Ollama or another local LLM.

Troubleshooting
- Module errors: re-run `pip install -r requirements.txt`.
- API errors: verify the environment variable value and network connectivity.
- Streamlit port issues: try `streamlit run ai_study.py --server.port 8502`.

Contributing
- Suggested improvements: add more study modes, persist sessions to disk, or add user authentication.

License
- MIT-style / free to use for educational purposes.

---
Updated README for concise setup, configuration, and usage.
- Try running: `streamlit run ai_study.py --logger.level=debug`
