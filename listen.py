import speech_recognition as sr
import pyttsx3
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text
# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say("Hello, I am your personal assistant. Say something to me, and I will recognize it.")
engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True  # Adapts to ambient noise

while True:
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            text = recognizer.recognize_google(audio)
            with open("recognized_speech.txt", "a", encoding="utf-8") as file:
                file.write(text + "\n")
                
            text = clean_text(text)
            print("You said:", text)

            engine.say(f"You said: {text}")
            engine.runAndWait()

            # Stop condition
            if "stop listening" in text.lower():
                print("Exit command received. Shutting down.")
                engine.say("Goodbye!")
                engine.runAndWait()
                break

        except sr.WaitTimeoutError:
            print("No speech detected. Waiting again...")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            engine.say("Sorry, I didn't catch that.")
            engine.runAndWait()
        except sr.RequestError as e:
            print(f"API error: {e}")
            engine.say("There's a problem with the recognition service.")
            engine.runAndWait()
