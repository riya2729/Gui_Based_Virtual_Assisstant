import speech_recognition as sr
import pyttsx3
from time import ctime
import time
import webbrowser
import random
import playsound
import os
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image


print('say something.....')
r = sr.Recognizer()
engine = pyttsx3.init()
   
def takeCommand(ask = False):
    with sr.Microphone() as source:
        
        if ask:
           al_voice(ask)
        audio = r.listen(source)
        query = ''
            
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio)
            print("User Said: " + query)
            
        except Exception as e:
            print(e)    
            print("Sorry! didn't get that,Please repeat...")  
            al_voice("Sorry! didn't get that,Please repeat...")  
        return query

def al_voice(audio_string):
    tts = gTTS(text = audio_string, lang = 'en-in')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

        
class Widget:
    def __init__(self): 
        window = Tk()
        window.geometry('520x320')
        window.title("Riya_12008120")
        window.configure(background ='black')
        icon = PhotoImage(file='ria.png')
        window.iconphoto(True, icon)


        im = ImageTk.PhotoImage(Image.open('img.png'))
        panel = Label(window, image = im)
        panel.pack(side = 'right', fill = 'both', expand = 'no')

        compText = StringVar()
        userText = StringVar()

        userText.set('Virtual Assitant\n    🤖')
        userFrame = LabelFrame(window, text='Alexa', font = ('Railway', 20, 'bold'))
        userFrame.pack(fill = 'both', expand = 'yes')

        one = Message(userFrame, textvariable=userText, bg = 'black', fg = 'beige')
        one.configure(font = ('Century Gothic', 20, 'bold'))
        one.pack(side = 'top', fill = 'both', expand = 'yes')

        btn1 = Button(window, text = 'speak', bg = 'red', fg = 'yellow', font = 'bold', command = self.clicked)
        btn1.pack(fill = 'x', expand = 'no')

        btn2 = Button(window, text = 'Clear', bg = 'yellow', fg = 'red',font = 'bold', command = window.destroy)
        btn2.pack(fill = 'x', expand = 'no')
        
        al_voice('How can i Help you?')  
        window.mainloop()
    
    def clicked(self):
        print('working.....')
        
        query = takeCommand()
        query = query.lower()
        
        if 'who are you' in query:
              al_voice('Hi! I am Alexa, your Virtual Assistant')
    
        if 'how are you' in query:
            al_voice('I am splendid, Thank you for asking')   
        
        if 'search' in query:
            search = takeCommand('What do you want to search?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            al_voice('This is your Search Result:' + search)
            
        if 'do one thing' in query:
            al_voice("I'll do what I can. What's up?")   
             
        if 'what can you do for me' in query:
            al_voice("I'll do what I can. What's up?")    
                
        if 'do me a favour' in query:
            al_voice("I'll do what I can. What's up?")    
                
        if 'find location' in query:
            locaton = takeCommand('What location do you want to search?')
            url = 'https://google.nl/maps/place/' + location + '/&map;'
            webbrowser.get().open(url)
            al_voice('This is the required location:' + location)
            
        if 'what is the time' in query:
            al_voice("Time is " + ctime())
        
        if 'thank you'in query:
            al_voice('I m Honoured to serve')  
        
        if 'exit ' in query:
            al_voice('Thank you have a good day')
            exit()
            
        if 'quit' in query:
            al_voice('Thank you have a good day')
            exit()
            
        if 'bye-bye' in query:
            al_voice('Thank you have a good day')
            exit()

    
    
def respond(query):
    pass
if __name__ == '__main__':
    widget = Widget()
       
time.sleep(1)

while 1:
    query = takeCommand()
    respond(query)

engine.runAndWait()