import pywhatkit as kit
import os
import pyttsx3
import time
from my_details import name
import traceback
import pygetwindow as gw

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def get_input(prompt):
    speak(prompt)
    return input(f"{prompt} ").lower().strip()

def send_whatsapp_message():
    try:
        contacts = {
            "mamy": "+917567110945",
            "papa": "+917434948356",
            "me": "+918320690850",
            "sudip": "+916354080767",
            "ayush": "+918140681519"
        }

        print("Mamy   Papa   Me   Sudip   Ayush")
        recipient = get_input("To whom do you want to send the message?")

        if recipient not in contacts:
            speak("Sorry, I couldn't find that contact.")
            return

        phone_number = contacts[recipient]
        message = get_input("What message would you like to send?")
        
        speak("Sending your message now, please wait.")
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True, close_time=5)
        
        label = "you" if recipient == "me" else "mom" if recipient == "mamy" else recipient
        speak(f"{name}, message sent successfully to {label}.")
        
        for window in gw.getWindowsWithTitle("Command Prompt"):
            print(f"Activating window: {window.title}")
            window.activate()
            if window.isMinimized:
                window.restore()
            window.activate()
            break     
        

    except Exception as e:
        print("[Detailed Traceback]:")
        traceback.print_exc()
        speak("Sorry, something went wrong.")
        
    finally:
        os.system("taskkill /f /im msedge.exe")
        
        return
        

if __name__ == "__main__":
    send_whatsapp_message()
