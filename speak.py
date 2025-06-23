import pyttsx3
import os
import sys
from my_details import name
import time
import psutil
import pyautogui

try:

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
    
    engine=pyttsx3.init()
    engine.say(f"Hello {name}, Welcome to your personal assistant")
    engine.runAndWait()
    while True:
        engine=pyttsx3.init()
        engine.say(f"What do you want to do?")
        engine.runAndWait()
        act=input("Action:- ")
        if act.lower()=="exit" or act.lower()=="bye":
            engine=pyttsx3.init()
            engine.say(f"Ok {name}, Do you want to close all oprn file??")
            engine.runAndWait()
            ans=input("Enter yes or no: ")
            if ans.lower()=="yes" or ans.lower()=="y":
                engine=pyttsx3.init()
                engine.say("Your personal assistant is closing all open file, have a nice day")
                engine.runAndWait()
                time.sleep(2)

                pyautogui.hotkey('ctrl', 'k')
                time.sleep(0.2)
                pyautogui.press('s')

                pyautogui.hotkey('ctrl', 'k')
                time.sleep(0.2)
                pyautogui.press('w')

                os.system("taskkill /f /im Code.exe")
              
            else:
                engine=pyttsx3.init()
                engine.say("Your personal assistant is closing, have a nice day")
                os.system("taskkill /f /im Code.exe")
        else:
            action(act.lower())
               


except Exception as e:
    print(e)