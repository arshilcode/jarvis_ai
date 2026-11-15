# import os
# import re
# import urllib.parse
# import urllib.request
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# SYSTEM_PROMPT = (
#     "You are Jarvis, a sharp, loyal, friendly, and witty personal AI assistant. "
#     "Talk like a smart, supportive friend in natural Hinglish (mix of Hindi and English). "
#     "Keep answers crisp, clear, and conversational (2 to 4 sentences max) because your replies "
#     "are spoken aloud. Never use markdown symbols like *, #, or bullet points. "
#     "If live web search context is provided, use it accurately to answer current facts."
# )

# chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]
# _ACTIVE_MODEL = None

# def get_active_model() -> str:
#     """Tumhare Groq account par available best active LLM model automatically select karega"""
#     global _ACTIVE_MODEL
#     if _ACTIVE_MODEL:
#         return _ACTIVE_MODEL

#     try:
#         models_data = client.models.list().data
#         excluded = ("whisper", "guard", "tts", "playai", "embed", "orpheus")
#         chat_models = [
#             m.id for m in models_data
#             if not any(bad in m.id.lower() for bad in excluded)
#         ]

#         preferences = [
#             "llama-4",
#             "llama-3.3",
#             "llama-3.1-70b",
#             "llama-3.1-8b",
#             "qwen",
#             "deepseek",
#             "gemma",
#             "mixtral",
#         ]
#         for pref in preferences:
#             for model_id in chat_models:
#                 if pref in model_id.lower():
#                     _ACTIVE_MODEL = model_id
#                     print(f"[Brain connected to model: {_ACTIVE_MODEL}]")
#                     return _ACTIVE_MODEL

#         if chat_models:
#             _ACTIVE_MODEL = chat_models[0]
#             print(f"[Brain connected to model: {_ACTIVE_MODEL}]")
#             return _ACTIVE_MODEL
#     except Exception:
#         pass

#     return "llama-3.1-8b-instant"

# def search_web_context(query: str) -> str:
#     """Current ya factual sawalon ke liye web se live snippet laata hai"""
#     try:
#         encoded = urllib.parse.quote(query)
#         url = f"https://html.duckduckgo.com/html/?q={encoded}"
#         req = urllib.request.Request(
#             url,
#             headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
#         )
#         html = urllib.request.urlopen(req, timeout=4).read().decode("utf-8", errors="ignore")
#         snippets = re.findall(r'class="result__snippet"[^>]*>(.*?)</a>', html, re.S)
#         clean_snippets = [re.sub(r"<.*?>", "", s).strip() for s in snippets[:3]]
#         return " | ".join(clean_snippets) if clean_snippets else ""
#     except Exception:
#         return ""

# def ask_jarvis(prompt: str) -> str:
#     """Live search aur memory ke saath smart Hinglish jawab deta hai"""
#     global chat_history

#     web_info = search_web_context(prompt)
#     if web_info:
#         user_message = (
#             f"User Question: {prompt}\n\n"
#             f"[Live Web Search Results for accuracy]: {web_info}"
#         )
#     else:
#         user_message = prompt

#     chat_history.append({"role": "user", "content": user_message})

#     if len(chat_history) > 11:
#         chat_history = [chat_history[0]] + chat_history[-10:]

#     try:
#         model_name = get_active_model()
#         response = client.chat.completions.create(
#             model=model_name,
#             messages=chat_history,
#             temperature=0.6,
#             max_tokens=220,
#         )
#         reply = response.choices[0].message.content.strip()
#         chat_history.append({"role": "assistant", "content": reply})
#         return reply
#     except Exception as e:
#         return f"Brain module mein dikkat aayi hai: {str(e)}"




import os
import re
import urllib.parse
import urllib.request
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = (
    "You are Jarvis, a sharp, loyal, and friendly personal AI assistant. "
    "Talk like a smart friend in natural Hinglish unless asked to switch languages. "
    "Keep answers crisp and conversational (2 to 4 sentences max) since they are spoken aloud. "
    "Avoid markdown symbols like *, #, or bullet points. "
    "Use the provided web search context whenever answering current factual queries."
)

history = [{"role": "system", "content": SYSTEM_PROMPT}]
active_model = None


def pick_model():
    global active_model
    if active_model:
        return active_model

    try:
        available = client.models.list().data
        skip = ("whisper", "guard", "tts", "playai", "embed", "orpheus")
        valid = [m.id for m in available if not any(x in m.id.lower() for x in skip)]

        priority = ["llama-4", "llama-3.3", "llama-3.1-70b", "llama-3.1-8b", "qwen", "gemma"]
        for tag in priority:
            for mid in valid:
                if tag in mid.lower():
                    active_model = mid
                    return active_model

        if valid:
            active_model = valid[0]
            return active_model
    except Exception:
        pass

    return "llama-3.1-8b-instant"


def fetch_web_snippet(query):
    try:
        q = urllib.parse.quote(query)
        url = f"https://html.duckduckgo.com/html/?q={q}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=4).read().decode("utf-8", errors="ignore")
        matches = re.findall(r'class="result__snippet"[^>]*>(.*?)</a>', html, re.S)
        cleaned = [re.sub(r"<.*?>", "", m).strip() for m in matches[:3]]
        return " | ".join(cleaned) if cleaned else ""
    except Exception:
        return ""


def ask_jarvis(prompt):
    global history

    context = fetch_web_snippet(prompt)
    if context:
        msg = f"Question: {prompt}\n\n[Web Context]: {context}"
    else:
        msg = prompt

    history.append({"role": "user", "content": msg})

    # Keep only recent 10 turns in memory
    if len(history) > 11:
        history = [history[0]] + history[-10:]

    try:
        res = client.chat.completions.create(
            model=pick_model(),
            messages=history,
            temperature=0.6,
            max_tokens=220,
        )
        reply = res.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as err:
        return f"Brain module mein dikkat aayi hai: {err}"