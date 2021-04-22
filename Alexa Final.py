#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ALEXA,a voice assisstant AI
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib 
import ctypes
import time
import subprocess
import string
import random
from ecapture import ecapture as ec
import requests




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("This is Alexa. How may I help you?")


def takeCommand():
    
    r=sr.Recognizer()
   
    print("Listening ...")
       
    r.pause_threshold=1
    with sr.Microphone() as source:
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    file=open("ur_text_file.txt","rt")   #file should store password
    password=file.read()
    file.close()
    
    mailDir={"Name":"email","name":"email"}
    server.login('ur_email_for_sending',password)
    server.sendmail('ur_email_for_sending',mailDir[to],content)
    server.close()



if __name__=='__main__':
    
    wishMe()
    chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    while True:
        query=takeCommand().lower()
        
        if 'send email' in query or "send mail" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                speak("To whom should I send the email?")
                to=takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email at the moment")
        
        elif "weather" in query:
             
           
            api_key = ""  #get api key from website openweather
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x['main']
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature (in kelvin unit) = " +
                        str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+
                        str(current_pressure) +"\n humidity (in percentage) = " +
                        str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
        
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get(chromepath).open('youtube.com')
        elif 'open google' in query:
            webbrowser.get(chromepath).open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.get(chromepath).open("stackoverflow.com")
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = ""  #specify your music directory
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        

        
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "camera" in query or "take a photo" in query:
            N = 7
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
            speak("Cheese!")
            speak("3")
            speak("2")
            speak("1")
            ec.capture(0, "Captured by Alexa ", "/images/"+res+".jpg")
            speak("Picture taken!")
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            
        
            
        elif "quit" in query or "close" in query:
            exit()


# In[ ]:




