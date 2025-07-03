# This is a speak_voice python file created by your personal assistant
#this is a solid example of a simple AI-powered personal assistant that interfaces directly with your operating system to handle basic 
# file operations with voice interaction

import pyttsx3
import os
import sys
from my_details import name
import time
import psutil
import pyautogui
import subprocess
import speech_recognition as sr


try:
    def create_file(file_name,file_type):
        if file_type=="text":
            file_name=input("Enter file name: ")
            data=input("Enter data: ")
            with open(f"{file_name}.txt","w") as file:
                file.write(data)
                engine=pyttsx3.init()
                engine.say(f"{name}, new text file is added in your directory, Do you want to open it?")
                engine.runAndWait()
                a=input("Enter yes or no: ")
                if a=="yes":
                    engine=pyttsx3.init()
                    engine.say(f"Opeaning file {file_name}")
                    file_name = file_name + ".txt"
                    os.startfile(file_name)
                    engine.runAndWait()
                else:
                    engine=pyttsx3.init()
                    engine.say("Something is wronge, please try again")
                    return
        elif file_type=="audio" or file_type=="mp3" or file_type=="voice":
                        
            engine=pyttsx3.init()
            engine.say("Enter the mp3 file name")
            engine.runAndWait()
            mp3_name=input("Enter mp3 file name: ")
            engine=pyttsx3.init()
            engine.say("Enter the mp3 data")
            engine.runAndWait()
            mp3_data=input("Enter mp3 data: ")
            engine.save_to_file(mp3_data,mp3_name)
            engine.runAndWait()

            mp3_decision=input("Do you want to open mp3 file??(yes/no)")
            mp3_name= mp3_name + ".mp3"
            engine.save_to_file(mp3_data,mp3_name)
            engine.runAndWait()
                        

            if mp3_decision.lower() == 'yes':
                os.startfile(mp3_name)
                time.sleep(2)
                return

            else:
                time.sleep(2)
                return
            
        elif file_type=="python" or file_type=="py":
            engine=pyttsx3.init()
            engine.say("Enter the python file name")
            engine.runAndWait()

            py_name=input("Enter python file name: ")

            with open(f"{py_name}.py","w") as file:
                file.write(f"# This is a {py_name} python file created by your personal assistant\n")

            engine=pyttsx3.init()
            engine.say(f"Ok Sir {py_name} python file is created, Do you want to open it?")
            engine.runAndWait()

            des=input("Enter yes or no: ")

            if des.lower()=="yes" or des.lower()=="y":
                os.startfile(f"{py_name}.py")

                engine=pyttsx3.init()
                engine.say(f"Opening {py_name} python file")
                engine.runAndWait()

    def search(file_name):
        exe=['.txt','.mp3','.py','.exe','.jpg','.png','.jpeg','.pdf','.docx','.pptx','.xlsx','.doc','.html','.css','.js']
        file_name_list=[file_name+i for i in exe]
        file = " "

        for file_name in file_name_list:
            if file_name in os.listdir():
                return file_name
        return None
                
    def action(value):
        match value:
            case "how many file in this folder" | "files in this folder":
                files=os.listdir()
                print(files)
                py=[i for i in files if i.endswith('.py')]
                text=[i for i in files if i.endswith('.txt')]
                mp3=[i for i in files if i.endswith('.mp3')]
                csv=[i for i in files if i.endswith('.csv')]
                pdf=[i for i in files if i.endswith('.pdf')]
                other=[i for i in files if not (i.endswith('.py') or i.endswith('.txt') or i.endswith('.mp3') or i.endswith('.csv') or i.endswith('.pdf'))]
                engine=pyttsx3.init()
                engine.say(f"{name}, there are {len(files)} files in this folder,Do you want to know the details of these files?")
                engine.runAndWait()
                decision=input("Enter yes or no: ")
                if decision.lower() in ['yes','y']:
                    engine=pyttsx3.init()
                    engine.say(f"There are {len(py)} python files, {len(text)} text files, {len(csv)} csv files, {len(pdf)} pdf files and {len(other)} other files in this folder")
                    engine.runAndWait()
                    engine=pyttsx3.init()
                    engine.say("Do you want to open any file?")
                    engine.runAndWait()
                    decision=input("Enter yes or no: ")
                    if decision.lower() in ['yes','y']:
                        engine=pyttsx3.init()
                        engine.say("Which file?")
                        engine.runAndWait()
                        file_name=input("Enter file name: ")
                        file=search(file_name)
                        if file:
                            engine=pyttsx3.init()
                            engine.say(f"{file} is founded, Do you want to open it?")
                            engine.runAndWait()

                            decision=input("Enter yes or no: ")

                            if decision.lower() == 'yes' or decision.lower() == 'y':
                                engine=pyttsx3.init()
                                engine.say(f"Opeaning file {file_name}")
                                os.startfile(file)
                                engine.runAndWait()
                                engine=pyttsx3.init()
                                engine.say(f"file is opened, you can read it now")
                        else:
                            engine=pyttsx3.init()
                            engine.say(f"Sorry {name}, file not found")
                            engine.runAndWait()



                
            case "read":
                engine=pyttsx3.init()
                engine.say("Which file do you want to read?")
                engine.runAndWait()

                file_name=input("Enter file name: ")
                file=search(file_name)

                if file:
                    engine=pyttsx3.init()
                    engine.say(f"{file} is founded, Do you want to open it?")
                    engine.runAndWait()

                    decision=input("Enter yes or no: ")

                    if decision.lower() == 'yes' or decision.lower() == 'y':

                        engine=pyttsx3.init()
                        engine.say(f"Opeaning file {file_name}")

                        os.startfile(file)
                        engine.runAndWait()
                        engine=pyttsx3.init()

                        engine.say(f"file is opened, you can read it now")

                else:
                    engine=pyttsx3.init()
                    engine.say(f"Sorry {name}, file not found")
                    engine.runAndWait()
                    return 
                
                sys.exit()

            case "write" | "store" | "create":
                engine=pyttsx3.init()
                engine.say("Which file do you want to make?")
                engine.runAndWait()

                file_type=input("Enter file type: ")
                create_file(file_name=None,file_type=file_type.lower())
                
                           
            case "delete" | "remove":
                engine=pyttsx3.init()
                engine.say("Which file do you want to delete?")
                engine.runAndWait()

                file_name=input("file name: ")
                file=search(file_name)

                print(file)
                
                if file:
                    os.remove(file)
                    engine=pyttsx3.init()
                    engine.say(f"{name}, {file} is deleted")
                    engine.runAndWait()
                    time.sleep(2)
                    return
                
                else:
                    print("File not found")
                    time.sleep(2)
                    return
                
            case "wifi on" | "on wifi":
                engine = pyttsx3.init()
                engine.say("Turning on Wi-Fi")
                engine.runAndWait()

                subprocess.run('netsh interface set interface name="Wi-Fi" admin=enable', shell=True)

                engine = pyttsx3.init()
                engine.say("Wifi is on")
                engine.runAndWait()

            case "close app" | "close application" | "close all app" | "close all application":
                engine=pyttsx3.init()
                engine.say("Closing all open application")
                engine.runAndWait()

                def is_process_running(process_name):
                    tasks = subprocess.check_output(['tasklist'], shell=True).decode()
                    return process_name.lower() in tasks.lower()

                def close_if_open(process_name):
                    if is_process_running(process_name):
                        os.system(f"taskkill /f /im {process_name}")
                    else:
                        print(f"{process_name} is not running.")

                apps_to_close = [
                    "chrome.exe",            
                    "WINWORD.EXE",   
                    "msedge.exe",    
                    "wps.exe",
                    "notepad.exe",    
                    "Taskmgr.exe",        
                ]

                for app in apps_to_close:
                    close_if_open(app)
                    time.sleep(1.5)

                engine=pyttsx3.init()
                engine.say("All open application is closed")
                engine.runAndWait()
                
            case _:

                engine=pyttsx3.init()
                engine.say(f"Sorry {name}, I don't know how to {value}")
                engine.runAndWait()
                time.sleep(2)
                return


    engine=pyttsx3.init()
    engine.setProperty('rate', 170)     
    engine.setProperty('volume', 0.9)   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  

    
    os.chdir(r"C:\Users\kansa\OneDrive\Desktop\my project")
    print(os.getcwd())
    #os.chdir(r"C:\Users\kansa\OneDrive\Desktop\ML\Projects")
    #os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    print("You can create, read, write, delete, and search files")
    print("You can also close all open applications, and shutdown your device")

    engine=pyttsx3.init()
    engine.say(f"Hello {name}, Welcome to your personal assistant")
    engine.runAndWait()

    while True:
        engine=pyttsx3.init()
        engine.say(f"What do you want to do?")
        engine.runAndWait()

        # Initialize recognizer
        recognizer = sr.Recognizer()
        recognizer.dynamic_energy_threshold = True  # Adapts to ambient noise

        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)
            act = recognizer.recognize_google(audio,language='en-IN')
            print(act)
            with open("recognized_speech.txt", "a", encoding="utf-8") as file:
                file.write(act + "\n")
            #act = cleant_text(act)
            if act.lower()=="exit" or act.lower()=="bye":
                engine=pyttsx3.init()
                engine.say(f"Ok {name}, Do you want to close all open file??")
                engine.runAndWait()

                ans=input("Enter yes or no: ")        
                if ans.lower()=="yes" or ans.lower()=="y":
                    engine=pyttsx3.init()
                    engine.say("Your personal assistant is Saving all open file, have a nice day")
                    engine.runAndWait()
                    time.sleep(2)

                    pyautogui.hotkey('ctrl', 'k')
                    time.sleep(0.2)
                    pyautogui.press('s')

                    pyautogui.hotkey('ctrl', 'k')
                    time.sleep(0.2)
                    pyautogui.press('w')

                    os.system("taskkill /f /im Code.exe")
                
                elif ans.lower()=="no" or ans.lower()=="n":
                    engine=pyttsx3.init()
                    engine.say("Your personal assistant is closing, have a nice day")
                    os.system("taskkill /f /im Code.exe")
                
            elif act.lower()=="shutdown" or act.lower()=="s" or act.lower()=="power off":
                    subprocess.call('netsh interface set interface name="Wi-Fi" admin=disable', shell=True)
                    subprocess.call('netsh interface set interface "Bluetooth Network Connection" admin=disable', shell=True)
                    engine=pyttsx3.init()
                    engine.say("Your personal assistant is Shutdown your device, please check that you all application is close")
                    engine.runAndWait()
                    os.system("shutdown /s /t 0")
                    continue
                    
            elif act.lower()=="restart" or act.lower()=="reboot":
                    subprocess.call('netsh interface set interface name="Wi-Fi" admin=disable', shell=True)
                    subprocess.call('netsh interface set interface "Bluetooth Network Connection" admin=disable', shell=True)
                    engine=pyttsx3.init()
                    engine.say("Your personal assistant is Restart your device, please check that you all application is close")
                    engine.runAndWait()
                    os.system("shutdown /r /t 0")
                    continue
            elif act.lower()=="close":
                sys.exit()

            elif "how are you" in act.lower() or "how are you doing" in act.lower():
                engine=pyttsx3.init()
                engine.say(f"I'm fine {name}, How are you?")
                engine.runAndWait()
                continue

            else:

                action(act.lower())
                


except Exception as e:
    print(e)