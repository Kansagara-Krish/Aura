import webbrowser as wb
import pyttsx3
import smtplib
import pythoncom 
from email.message import EmailMessage

def open_mail():
   
    email={1:"kansagara.krish2006@gmail.com",2:"23012011026@gmail.com"}
    print("1.kansagara.krish2006@gmail.com\n2.23012011026@gnu.ac.in")
    print("Enter your choice: ",)
    choice = int(input())
    if choice in email:
        print(f"Opening {email[choice]} in your browser...")

    index=email.get(choice)
    url=f"https://mail.google.com/mail/u/0/#inbox?compose=new&to={index}"
    print(f"Opening URL: {url}")
    wb.open(url)

def send_mail(to,content):
    try:
        pythoncom.CoInitialize()
        msg = EmailMessage()
        msg['Subject'] = 'Mail by Krish'
        msg['From'] = 'kansagara.krish2006@gmail.com'
        msg['To'] = to
        
        msg.set_content(content)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('kansagara.krish2006@gmail.com', 'bbqm vyyi ucjx lfuu')
            smtp.send_message(msg)

        return True 

    except Exception as e:
        print(f"Error: {e}")
        return False 
    
    finally:
        pythoncom.CoUninitialize()
    
if __name__ == "__main__":
    send_mail()
    print("Mail opened successfully.")