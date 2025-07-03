import google.generativeai as genai

def code(prompt):
    API_KEY="AIzaSyCIo6crX_Xj6Qnf4aoOOQZVepVyLGpWs_s"

    genai.configure(api_key=API_KEY)

    model=genai.GenerativeModel("gemini-2.5-flash")

    chat=model.start_chat()
       
    respose=chat.send_message(prompt+" give me just full code no comment no extra text in your reply")
    print("Gemini:",respose.text)
    
    return respose.text

if __name__=="__main__":
    code("hello")