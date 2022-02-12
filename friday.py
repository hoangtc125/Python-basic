import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[0].id)

def speak(audio):
    print("F.R.I.D.A.Y:", audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Cong Hoang")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Cong Hoang")
    else:
        speak("Good night Cong Hoang")
    speak("How can I help you")

def command():
    c = sr.Recognizer() 
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language = "en")
        print("Cong Hoang:", query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('Your order is: '))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("what should i search Cong Hoang")
            search = command().lower()
            url = f"http://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("what should i search Cong Hoang")
            search = command().lower()
            url = f"http://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        if "application" in query:
            speak("what should i search Cong Hoang")
            search = command().lower()
            link = r"C://Users//ADMIN//Desktop//" + search
            os.startfile(link)
        if "time" in query:
            time()
        if "quit" in query:
            speak("Goodbye Cong Hoang")
            quit()
