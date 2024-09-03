# http://qiniucdn.star-lai.cn/portal/2016/09/05/tu3p2vd4znn

import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import openai
import datetime
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
         print("Recognizing..... ")
         query = r.recognize_google(audio, language ="en-in")
         print(f"User said: {query}")
         return query
        except Exception as e:
         return "some error occured, Sorry from Jarvis"

if __name__ == '__main__':
    print("python")
    say("Hello I'm Speaking from Ohio Town of North Carolina, US. What can i do for you",lang='en-in')
    while True:
      print("Listening.....")
      query = takeCommand()
      sites = [["youtube", "https://www.youtube.com"],["wikipedia","https://www.wikipedia.org/"],["linkedin","https://www.linkedin.com/feed/"],["यूट्यूब खोलो","https://www.youtube.com"],["विकिपीडिया खोलो","https://www.wikipedia.org/"],["लिंकडइन खोलो","https://www.linkedin.com/feed/"]]  
      for site in sites:
       if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} Sir... ")
            webbrowser.open(site[1])
       if "open movie" in query:
            musicPath = "D:\ALL MOVIES\HOLLYWOOD MOVIES\www.9xflix.com - Iron Man 3 (2013) Dual Audio Hindi 480p BluRay.mkv"
            os.startfile(musicPath)
       if "फिल्म दिखाओ" in query:
            musicPath = "D:\ALL MOVIES\HOLLYWOOD MOVIES\www.9xflix.com - Iron Man 3 (2013) Dual Audio Hindi 480p BluRay.mkv"
            os.startfile(musicPath)
       if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")
       if "समय बताओ" in query:
            hour = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            seconds = datetime.datetime.now().strftime("%S")
            say(f"Sir the time is {hour} bazzgjkaar {minutes} auor {seconds} seconds hoo rahaa hai")