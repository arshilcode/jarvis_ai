# Jarvis AI Assistant

A modular personal desktop assistant built in Python for Windows. It combines speech recognition, Groq LLM inference, live web search context, and OS automation.

## Structure
- `main.py` — Entry point and voice/text mode loop
- `core/voice.py` — Speech-to-text (Google SR) and offline TTS (SAPI5)
- `core/brain.py` — Groq chat completions, auto model selection, and web context lookup
- `core/actions.py` — App launcher, browser shortcuts, battery check, volume, and screenshots
- `core/music_library.py` — Local song map with YouTube search fallback

## Local Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt