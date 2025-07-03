#this is a solid example of a simple AI-powered personal assistant that interfaces directly with your operating system to handle basic 
# file operations with voice interaction



try:
    import pyttsx3
    import os
    import find_file
    import mail
    from my_details import name
    import whattup
    import webbrowser
    import time
    import sys
    import pyautogui
    import pytesseract
    from PIL import Image
    import subprocess
    from datetime import datetime
    from datetime import date
    import google.generativeai as genai
    import csv
    import threading
    import pythoncom 
    import smtplib
    import pythoncom 
    from email.message import EmailMessage
    from inputimeout import inputimeout, TimeoutOccurred
    import random
    
    def input_with_timeout(prompt="Enter command: ", timeout=20):
            timeout_messages = [
                f"{name}, are you still there?",
                f"Hello {name}, are you with me?",
                f"{name}, I'm waiting for your command...",
                f"Did you forget about me, {name}?",
                f"{name}, should I keep waiting?",
                f"Just checking in, {name}...",
                f"{name}, let me know if you need anything!"
            ]
        
            try:
                return inputimeout(prompt=prompt, timeout=timeout)
            except TimeoutOccurred:
                message = random.choice(timeout_messages)
                
                try:
                    engine = pyttsx3.init()
                    engine.say(message)
                    engine.runAndWait()
                except Exception as e:
                    print(f"Voice error: {e}")
                
                return ""

    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    def code(prompt):
        API_KEY="AIzaSyCIo6crX_Xj6Qnf4aoOOQZVepVyLGpWs_s"

        genai.configure(api_key=API_KEY)

        model=genai.GenerativeModel("gemini-2.5-flash")

        chat=model.start_chat()
        
        response = chat.send_message(prompt + " — return only the complete code in plain text format without markdown, backticks, or extra formatting. I want to directly run the code.")
        
        return response.text

    def create_file(file_name,file_type):
        engine=pyttsx3.init()
        engine.say("In which folder do you want to create?")
        engine.runAndWait()
        
        des=input("Folder name:")
        if des.lower()=="desktop":
            pass
        else:
            path=find_file.find_folder(des)
            os.chdir(path)
            
        last_name=os.path.basename(os.getcwd())
        
        if file_type=="text":
            file_name=input("Enter file name: ")
            data=input("Enter data: ")
            with open(f"{file_name}.txt","w") as file:
                file.write(data)
                engine=pyttsx3.init()
                engine.say(f"{name}, new text file is added in {last_name}, Do you want to open it?")
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
            engine=pyttsx3.init()
            engine.say("SIR do you want to add any code in this file?")
            engine.runAndWait()
            
            des=input("Enter Yes or no: ")
            
            if des.lower() in ["yes",'y']:
                engine=pyttsx3.init()
                engine.say("Which kind of code do you want to add?")
                engine.runAndWait()
                prompt=input("Enter the prompt:- ")
                print("🤖 Working on that...")
                py_code=code(prompt)
                
            with open(f"{py_name}.py","w") as file:
                file.write(f"# This is a {py_name} python file created by your personal assistant\n{py_code}")

            engine=pyttsx3.init()
            engine.say(f"Ok Sir {py_name} python file is created in {last_name} folder, Do you want to open it or directly run?")
            engine.runAndWait()

            des=input("Enter run or open: ")

            if des.lower()=="open" or des.lower()=="o":
                os.startfile(f"{py_name}.py")

                engine=pyttsx3.init()
                engine.say(f"Opening {py_name} python file")
                engine.runAndWait()
            
            elif des.lower() in ["run",'r']:
                subprocess.run(["python", py_name+".py"])
                
        elif file_type=="html" or file_type=="ht":
            engine=pyttsx3.init()
            engine.say("Enter the html file name")
            engine.runAndWait()

            html_name=input("Enter html file name: ")
            engine=pyttsx3.init()
            engine.say("SIR do you want to add any code in this file?")
            engine.runAndWait()
            
            des=input("Enter Yes or no: ")
            
            if des.lower() in ["yes",'y']:
                engine=pyttsx3.init()
                engine.say("Which kind of code do you want to add?")
                engine.runAndWait()
                prompt=input("Enter the prompt:- ")
                print("🤖 Working on that...")
                html_code=code(prompt)
                
            with open(f"{html_name}.html","w") as file:
                file.write(f"<!-- This is a {name} python file created by your personal assistant-->\n{html_code}")

            engine=pyttsx3.init()
            engine.say(f"Ok Sir {html_name} python file is created in {last_name} folder, Do you want to open it or directly run?")
            engine.runAndWait()

            des=input("Enter run or open: ")

            if des.lower()=="open" or des.lower()=="o":
                os.startfile(f"{html_name}.html")

                engine=pyttsx3.init()
                engine.say(f"Opening {html_name} python file")
                engine.runAndWait()
            
            elif des.lower() in ["run",'r']:
                subprocess.run(["html", html_name+".html"])
                
    def search(file_name):
        exe=['.txt','.csv','.mp3','.py','.exe','.jpg','.png','.jpeg','.pdf','.docx','.pptx','.xlsx','.doc','.html','.css','.js']
        file_name_list=[file_name+i for i in exe]
        file = " "

        for file_name in file_name_list:
            if file_name in os.listdir():
                return file_name
        return None
                
    def action(value):
        match value:
            case "in which folder i am" | "in which folder am i" | "in which folder am i currently" | "current folder" | "current directory" | "where i am" | "where am i":
                current_folder = os.getcwd()
                current_folder=os.path.basename(current_folder)
                engine=pyttsx3.init()
                engine.say(f"You are currently in {current_folder}")
                engine.runAndWait()
                
                return
            
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
          
            case "whatsapp" | "whattup" | "whats app" | "whatsap":
                engine=pyttsx3.init()
                engine.say("Opening WhatsApp")
                engine.runAndWait()
                
                webbrowser.open("https://web.whatsapp.com")
 
                engine=pyttsx3.init()
                engine.say("WhatsApp is opened, you can check your messages now")
                engine.runAndWait()
                
                
            case "send message" | "send whatsapp message":
                engine=pyttsx3.init()
                engine.say("Do you want to send whatsapp message?")
                engine.runAndWait()

                decision=input("Enter yes or no: ")
                if decision.lower() in ['yes','y']:
                    whattup.send_whatsapp_message()
                    return
                else:
                    return
                
            case "how many folder" | "folder in folder"| "how many folder in this directory" | "how many folder in this directory i am" | "how many folder in this directory am i currently":
                folders = [f for f in os.listdir() if os.path.isdir(f)]
                engine=pyttsx3.init()
                engine.say(f"{name}, there are {len(folders)} folders in this directory")
                engine.runAndWait()
                print(folders)
                engine=pyttsx3.init()
                engine.say("Do you want to open any folder?")
                engine.runAndWait()
                
                des=input("Enter yes or no: ")
                if des.lower() in ['yes','y']:
                  
                   
                   messages=["Hmm, that doesn't seem right. Want to try another folder?",
                    "Still no match. Maybe double-check the name and give it another shot.",
                    "Oops! Folder not found. One more go?",
                    f"Hey {name}, I still couldn’t locate it. Try a different folder name?",
                    "That folder slipped past me. Type another?"]
                   
                   max_attempts = 3
                   attempts = 0
                   find_folder = False
                   
                   while not find_folder and attempts < max_attempts:
                        folder_name = input("Enter folder name: ").strip()
                        current_dir = os.getcwd()
                        folders = os.listdir(current_dir)
                        
                        if folder_name in folders and os.path.isdir(os.path.join(current_dir, folder_name)):
                            current_dir = os.getcwd()
                            folders = os.listdir(current_dir)
                            os.startfile(current_dir + "\\" + folder_name)
                            engine=pyttsx3.init()
                            engine.say(f"Folder is opened")
                            engine.runAndWait()
                            find_folder = True
                        else:
                            engine.say(messages[attempts % len(messages)])
                            engine.runAndWait()
                            attempts += 1

               
                
            case "open":
                engine=pyttsx3.init()
                engine.say("What do you want to open?")
                engine.runAndWait()

                file_name=input("Enter file name: ")
               
                csw,file_name=find_file.find_file_path(file_name)
                os.chdir(csw)
                print(csw)
                if csw:
                    engine=pyttsx3.init()
                    engine.say(f"file is founded, Do you want to open it?")
                    engine.runAndWait()

                    decision=input("Enter yes or no: ")

                    if decision.lower() == 'yes' or decision.lower() == 'y':

                        engine=pyttsx3.init()
                        engine.say(f"Opeaning file {file_name}")

                        os.startfile(file_name)
                        engine.runAndWait()
                        engine=pyttsx3.init()

                        engine.say(f"file is opened, you can read it now")
                        return
                    else:
                        return

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
                csw,file_name=find_file.find_file_path(file_name)
                
                os.chdir(csw)
                print(csw)
                last_name=os.path.basename(csw)
                engine=pyttsx3.init()
                engine.say(f"Do you want to delete {file_name} which is in Folder {last_name}?")
                engine.runAndWait()
                decision=input("Enter yes or no: ")
                if decision in ['yes','y']:
                    if file_name:
                        os.remove(file_name)
                        engine=pyttsx3.init()
                        engine.say(f"{name}, {file_name} is deleted")
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
                   

                apps_to_close = [
                    "chrome.exe",            
                    "WINWORD.EXE",   
                    "msedge.exe",    
                    "wps.exe",
                    "notepad.exe",    
                    "Taskmgr.exe", 
                    "Code.exe"       
                ]

                for app in apps_to_close:
                    close_if_open(app)
                    time.sleep(1.5)

                engine=pyttsx3.init()
                engine.say("All open application is closed")
                engine.runAndWait()
                
            case "mail" | "gmail":
                mail.open_mail()
                engine=pyttsx3.init()
                engine.say("Opening Gmail")
                engine.runAndWait()
                
            case "ai" | "copilot":

                edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"

                webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get('edge').open("https://copilot.microsoft.com")
            case _:

                engine=pyttsx3.init()
                engine.say(f"Sorry {name}, I don't know how to {value}")
                engine.runAndWait()
                time.sleep(2)
                return


    engine=pyttsx3.init()
    engine.setProperty('rate', 170)     
    engine.setProperty('volume', 1.0)   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  

    
    os.chdir(r"C:\Users\kansa\OneDrive\Desktop")
    print(os.getcwd())
    print("Version 2")
    print("You can create, read, write, delete, and search files")
    print("You can also close all open applications, and shutdown your device")


    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if current_time < "12:00:00":
        engine=pyttsx3.init()
        engine.say(f"Good morning SIR, How can I help you today?")
        engine.runAndWait()

    elif "12:00:00" <= current_time < "16:00:00":
        engine=pyttsx3.init()
        engine.say(f"Good afternoon SIR, How can I help you today?")
        engine.runAndWait()
        
    elif "16:00:00" <= current_time < "22:00:00":
        engine=pyttsx3.init()
        engine.say(f"Good evening SIR, How can I help you today?")
        engine.runAndWait()

    elif current_time >= "22:00:00":
        engine=pyttsx3.init()
        engine.say(f"Hey {name}, it's getting late. Time to recharge for tomorrow. Sweet dreams!")
        engine.runAndWait()
        sys.exit()
        
    file_path = r"C:\Users\kansa\OneDrive\Desktop\my project\details.csv"
    
    if not os.path.exists(file_path):
        with open(file_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date","Uses"])
        print("New file created")
            
    
    with open(file_path, "r+", newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

        today_str = date.today().isoformat()

        if rows:
            last_row = rows[-1]

            if last_row[0] == today_str:
                last_row[1] = str(int(last_row[1]) + 1)  
                rows[-1] = last_row  
            else:
                rows.append([today_str, "1"])
        else:
            rows.append([today_str, "0"])

        f.seek(0)
        f.truncate()
        writer = csv.writer(f)
        writer.writerows(rows)  
              
        
    while True:

            act = input_with_timeout("Enter your command: ")
            if not act:
                continue
            if act.lower()=="exit" or act.lower()=="bye":
                engine=pyttsx3.init()
                engine.say(f"Ok {name}, Do you want to off??")
                engine.runAndWait()

                ans=input("Enter yes or no: ")        
                if ans.lower()=="yes" or ans.lower()=="y":
                    engine=pyttsx3.init()
                    engine.say("Your personal assistant is Closing, Have a nice day")
                    engine.runAndWait()
                    time.sleep(2)

                    os.system("taskkill /f /im cmd.exe")

                
                elif ans.lower()=="no" or ans.lower()=="n":
                    engine=pyttsx3.init()
                    engine.say("Aura is still running, you can give me command")
                
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
                engine=pyttsx3.init()
                engine.say("Closing Aura, Have a nice day")
                engine.runAndWait()
                sys.exit()

            elif "how are you" in act.lower() or "how are you doing" in act.lower():
                engine=pyttsx3.init()
                engine.say(f"I'm fine {name}, How are you?")
                engine.runAndWait()
                continue

            else:
                action(act)
                break
                


except ValueError as e:
    print(e)
    
except ModuleNotFoundError as e:
    missing = str(e).split("'")[1]  
    print(f"Module '{missing}' not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", missing])
    print(f"Module '{missing}' installed successfully!")

    globals()[missing] = __import__(missing)