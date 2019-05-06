
import webbrowser
import smtplib
import random
import wolframalpha
from pyttsx3 import *
import speech_recognition as sr
import wikipedia
import datetime

import os
import sys
engine=pyttsx3.init('sapi5')
client=wolframalpha.Client('33A8LX-5HLWRG2Y9R')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)


def speak(audio):
    print("Computer:"+ audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    current_hr=int(datetime.datetime.now().hour)
    if current_hr>=0 and current_hr<12:
        speak('Good Morning!')
    if current_hr>=12 and current_hr<18:
        speak('Good Afternoon')
    if current_hr>=18 and current_hr!=0:
        speak('Good Night')
greetMe()

speak("Hello,I am your digital assistant!")
speak("What kind of help do you require?")


def myCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("hey!I am Listening!")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language="en-in")
        print('user'+ query+'\n')
    except sr.UnknownValueError:
        speak("Sorry Sir!I didn't get that")
        query=str(input('Command:'))
    return query

if __name__=='__main__':
    while True:
        query=myCommand();
        query=query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'how are you' in query:
            speak('okay')
            stMsgs=['Just Doing My Thing!','I am fine','Nice!']
            speak(random.choice(stMsgs))
        elif 'email' in query:
            speak('who is the recipient')
            recipient=myCommand()
            if 'me' in recipient:
                try:
                    speak('What is the message?')
                    content=myCommand()

                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')    

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
       
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        