import os
import smtplib#to send mails
import webbrowser
import time
def show_menu():
    print("can open notepad")
    print("can open control panel")
    print("can send mail")
    print("can open google")
    print("can open youtube")
    print("send whatsapp  messages")
    print("Play music online")
    
def whatsapp_msg(msg):
    numbers=919125072370
    for i in numbers:
        url = "https://wa.me/{}?text={}".format(i,msg)
        webbrowser.open(url)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    m_id=input("enter id ->")
    password=input("enter pass ->")
    server.login(m_id, password)
    server.sendmail(m_id, to, content)
    server.close()
def takeCommand(query):
    if "whatsapp" in query:
        msg=input("enter msg to send to whatsapp buddies")
        whatsapp_msg(msg)
    elif "control panel" in query:
        os.startfile("C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
    elif "notepad" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
   
    elif "menu" in query:
        show_menu()        
    elif 'youtube' in query.lower(): 
        webbrowser.open("youtube.com")
    elif 'google' in query:
        webbrowser.open("google.com")
    elif 'music' in query:
        webbrowser.open("https://gaana.com/")      
   
   
    
    elif "mail" or "email" in query:
        to=input("enter receiver mail ->")
        content=input("enter content you want to send ->")
        sendEmail(to,content)
    elif "whatsapp" in query:
        msg=input("enter msg to send to whatsapp buddies:  ")
        whatsapp_msg(msg)
    else:    
        print("!Not Found!sorry....will come with new update soon and will encounter your query too!!")
        

while __name__ == "__main__":
    name=input("enter your name sir/mam: ")
    print("Hello ..........{}".format(name))
    print("What do you want me to do?")
    show_menu()
    query=input()
    time.sleep(5)
    takeCommand(query)
