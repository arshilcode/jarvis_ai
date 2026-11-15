# import os
# import webbrowser
# import urllib.parse
# from datetime import datetime
# import psutil
# import pyautogui
# from AppOpener import open as app_open, close as app_close
# from core.voice import speak
# from core.music_library import play_song

# # Popular websites ke direct links
# WEBSITES = {
#     "youtube": "https://www.youtube.com",
#     "google": "https://www.google.com",
#     "whatsapp": "https://web.whatsapp.com",
#     "watsapp": "https://web.whatsapp.com",
#     "instagram": "https://www.instagram.com",
#     "github": "https://github.com",
#     "gmail": "https://mail.google.com",
#     "chatgpt": "https://chat.openai.com",
# }

# # Windows built-in tools
# SYSTEM_APPS = {
#     "settings": "start ms-settings:",
#     "calculator": "calc",
#     "notepad": "notepad",
#     "vs code": "code",
#     "code": "code",
#     "cmd": "start cmd",
#     "terminal": "start wt",
#     "file explorer": "explorer",
#     "this pc": "explorer",
#     "task manager": "taskmgr",
# }

# def execute_command(command: str) -> bool:
#     """System commands, apps, aur music handle karega"""
#     cmd = command.lower().strip()

#     # 1. Gaana bajana (e.g., "play kesariya" ya "chaleya song chalao")
#     if cmd.startswith("play ") or "gana chalao" in cmd or "song chalao" in cmd:
#         song = cmd.replace("play ", "").replace("gana chalao", "").replace("song chalao", "").strip()
#         if song:
#             status = play_song(song)
#             speak(status)
#             return True

#     # 2. Google par kuch search karna (e.g., "search python roadmap")
#     if cmd.startswith("search ") or "google par search" in cmd:
#         query = cmd.replace("search ", "").replace("google par search", "").strip()
#         if query:
#             speak(f"Google par {query} search kar raha hoon.")
#             webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(query)}")
#             return True

#     # 3. Koi bhi App ya Website kholna (e.g., "open chrome", "open spotify", "open whatsapp")
#     if cmd.startswith("open ") or "kholo" in cmd:
#         target = cmd.replace("open ", "").replace("kholo", "").strip()

#         # Check websites
#         for site, url in WEBSITES.items():
#             if site == target:
#                 speak(f"{site.capitalize()} khol raha hoon.")
#                 webbrowser.open(url)
#                 return True

#         # Check Windows built-in apps
#         for app_name, sys_cmd in SYSTEM_APPS.items():
#             if app_name == target:
#                 speak(f"{app_name.capitalize()} launch kar raha hoon.")
#                 os.system(sys_cmd)
#                 return True

#         # Laptop ka koi bhi installed app kholna (AppOpener)
#         try:
#             speak(f"{target} kholne ki koshish kar raha hoon.")
#             app_open(target, match_closest=True, output=False)
#             return True
#         except Exception:
#             speak(f"Mujhe {target} naam ka app laptop mein nahi mila.")
#             return True

#     # 4. Koi bhi App band karna (e.g., "close chrome", "close notepad")
#     if cmd.startswith("close ") or "band karo" in cmd:
#         target = cmd.replace("close ", "").replace("band karo", "").strip()
#         try:
#             speak(f"{target} band kar raha hoon.")
#             app_close(target, match_closest=True, output=False)
#             return True
#         except Exception:
#             speak(f"{target} band nahi ho paya.")
#             return True

#     # 5. Time aur Date
#     if "time" in cmd or "samay" in cmd:
#         now = datetime.now().strftime("%I:%M %p")
#         speak(f"Abhi {now} ho rahe hain.")
#         return True

#     if "date" in cmd or "tarikh" in cmd:
#         today = datetime.now().strftime("%d %B %Y")
#         speak(f"Aaj {today} hai.")
#         return True

#     # 6. Laptop Battery Check
#     if "battery" in cmd or "charge" in cmd:
#         battery = psutil.sensors_battery()
#         if battery:
#             status = "charging par hai" if battery.power_plugged else "battery par chal raha hai"
#             speak(f"Laptop mein {battery.percent} percent battery hai aur abhi {status}.")
#         else:
#             speak("Battery status read nahi ho pa raha.")
#         return True

#     # 7. Volume Control
#     if "volume up" in cmd or "awaaz badhao" in cmd:
#         pyautogui.press("volumeup", presses=5)
#         speak("Volume badha diya hai.")
#         return True

#     if "volume down" in cmd or "awaaz kam" in cmd:
#         pyautogui.press("volumedown", presses=5)
#         speak("Volume kam kar diya hai.")
#         return True

#     if "mute" in cmd:
#         pyautogui.press("volumemute")
#         speak("Audio mute toggle kar diya hai.")
#         return True

#     # 8. Screenshot Lena
#     if "screenshot" in cmd:
#         filename = f"screenshot_{datetime.now().strftime('%H%M%S')}.png"
#         pyautogui.screenshot(filename)
#         speak(f"Screenshot le kar {filename} naam se save kar diya hai.")
#         return True

#     return False







import os
import webbrowser
import urllib.parse
from datetime import datetime
import psutil
import pyautogui
from AppOpener import open as app_open, close as app_close
from core.voice import speak
from core.music_library import play_song

SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "whatsapp": "https://web.whatsapp.com",
    "watsapp": "https://web.whatsapp.com",
    "instagram": "https://www.instagram.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
}

WIN_APPS = {
    "settings": "start ms-settings:",
    "calculator": "calc",
    "notepad": "notepad",
    "vs code": "code",
    "code": "code",
    "cmd": "start cmd",
    "terminal": "start wt",
    "file explorer": "explorer",
    "this pc": "explorer",
    "task manager": "taskmgr",
}


def execute_command(command):
    cmd = command.lower().strip()

    if cmd.startswith("play ") or "gana chalao" in cmd or "song chalao" in cmd:
        song = cmd.replace("play ", "").replace("gana chalao", "").replace("song chalao", "").strip()
        if song:
            speak(play_song(song))
            return True

    if cmd.startswith("search ") or "google par search" in cmd:
        q = cmd.replace("search ", "").replace("google par search", "").strip()
        if q:
            speak(f"Google par {q} search kar raha hoon.")
            webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(q)}")
            return True

    if cmd.startswith("open ") or "kholo" in cmd:
        target = cmd.replace("open ", "").replace("kholo", "").strip()

        if target in SITES:
            speak(f"{target.capitalize()} khol raha hoon.")
            webbrowser.open(SITES[target])
            return True

        if target in WIN_APPS:
            speak(f"{target.capitalize()} launch kar raha hoon.")
            os.system(WIN_APPS[target])
            return True

        try:
            speak(f"{target} kholne ki koshish kar raha hoon.")
            app_open(target, match_closest=True, output=False)
            return True
        except Exception:
            speak(f"Mujhe {target} naam ka app laptop mein nahi mila.")
            return True

    if cmd.startswith("close ") or "band karo" in cmd:
        target = cmd.replace("close ", "").replace("band karo", "").strip()
        try:
            speak(f"{target} band kar raha hoon.")
            app_close(target, match_closest=True, output=False)
            return True
        except Exception:
            speak(f"{target} band nahi ho paya.")
            return True

    if "time" in cmd or "samay" in cmd:
        speak(f"Abhi {datetime.now().strftime('%I:%M %p')} ho rahe hain.")
        return True

    if "date" in cmd or "tarikh" in cmd:
        speak(f"Aaj {datetime.now().strftime('%d %B %Y')} hai.")
        return True

    if "battery" in cmd or "charge" in cmd:
        bat = psutil.sensors_battery()
        if bat:
            state = "charging par hai" if bat.power_plugged else "battery par chal raha hai"
            speak(f"Laptop mein {bat.percent} percent battery hai aur abhi {state}.")
        else:
            speak("Battery status read nahi ho pa raha.")
        return True

    if "volume up" in cmd or "awaaz badhao" in cmd:
        pyautogui.press("volumeup", presses=5)
        speak("Volume badha diya hai.")
        return True

    if "volume down" in cmd or "awaaz kam" in cmd:
        pyautogui.press("volumedown", presses=5)
        speak("Volume kam kar diya hai.")
        return True

    if "mute" in cmd:
        pyautogui.press("volumemute")
        speak("Audio mute toggle kar diya hai.")
        return True

    if "screenshot" in cmd:
        fname = f"screenshot_{datetime.now().strftime('%H%M%S')}.png"
        pyautogui.screenshot(fname)
        speak(f"Screenshot le kar {fname} naam se save kar diya hai.")
        return True

    return False