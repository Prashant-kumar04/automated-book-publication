import pyttsx3

def speak_text(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    with open("data/chapter_final.txt", "r") as f:
        final = f.read()
    speak_text(final)