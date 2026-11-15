from core.voice import speak, listen
from core.actions import execute_command
from core.brain import ask_jarvis


def main():
    speak("Jarvis is activated. Tum kisme comfortable ho, text format mein ya speach mein?")
    choice = input("\nType [text] ya [voice]: ").strip().lower()

    if any(w in choice for w in ["voice", "bol", "speak", "1"]):
        mode = "voice"
        speak("Done! Voice mode active hai. Bolo kya kaam hai?")
    else:
        mode = "text"
        speak("Done! Text mode active hai. Likho kya kaam hai, main bol kar jawab dunga.")

    while True:
        if mode == "voice":
            command = listen()
            if not command:
                continue
        else:
            command = input("\nYou: ").strip()
            if not command:
                continue

        if any(w in command.lower() for w in ["exit", "quit", "bye", "band ho ja", "sleep"]):
            speak("Shutting down. Jab zaroorat ho bula lena!")
            break

        if not execute_command(command):
            reply = ask_jarvis(command)
            speak(reply)


if __name__ == "__main__":
    main()