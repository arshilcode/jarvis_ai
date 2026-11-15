# import re
# import speech_recognition as sr
# import pyttsx3

# def speak(text: str):
#     """Jarvis ki awaaz mein bol kar output dega (Text aur Voice dono modes mein)"""
#     clean_text = re.sub(r"[*#`]", "", text).strip()
#     print(f"\nJarvis: {clean_text}")

#     try:
#         engine = pyttsx3.init("sapi5")
#         voices = engine.getProperty("voices")
#         engine.setProperty("voice", voices[0].id)  # 0 = Male voice, 1 = Female voice
#         engine.setProperty("rate", 180)
#         engine.say(clean_text)
#         engine.runAndWait()
#         engine.stop()
#     except Exception as e:
#         print(f"[Voice Error]: {e}")

# def listen() -> str:
#     """Mic se awaaz sun kar text mein badlega"""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("\nListening...")
#         recognizer.pause_threshold = 0.8
#         recognizer.adjust_for_ambient_noise(source, duration=0.4)
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         command = recognizer.recognize_google(audio, language="en-IN")
#         print(f"You: {command}")
#         return command.lower()
#     except sr.UnknownValueError:
#         return ""
#     except sr.RequestError:
#         speak("Internet connection check karo, speech recognition kaam nahi kar raha.")
#         return ""





import re
import speech_recognition as sr
import pyttsx3


def speak(text):
    clean = re.sub(r"[*#`]", "", text).strip()
    print(f"\nJarvis: {clean}")

    try:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 180)
        engine.say(clean)
        engine.runAndWait()
        engine.stop()
    except Exception as err:
        print(f"TTS error: {err}")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language="en-IN")
        print(f"You: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Internet connection check karo, speech recognition kaam nahi kar raha.")
        return ""