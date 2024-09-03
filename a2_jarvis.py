# http://qiniucdn.star-lai.cn/portal/2016/09/05/tu3p2vd4znn
   
import pyttsx3
import speech_recognition as sr
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
         query = r.recognize_google(audio, language ="hi-in")
         print(f"User said: {query}")
         return query
        except Exception as e:
         return "some error occured, Sorry from Jarvis"

if __name__ == '__main__':
    print("python")
    say("Hello I am Jarvis A.i")
    while True:
     print("Listening.....")
     text = takeCommand()
     say(text)