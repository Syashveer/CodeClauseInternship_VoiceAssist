import pyttsx3
import datetime
import os
import speech_recognition as sr
import pywhatkit as kit
import time
import wikipedia
import webbrowser
import pyautogui
from requests import get

keshava = pyttsx3.init('sapi5')
voices = keshava.getProperty('voices')
keshava.setProperty('voices', voices[0].id)

def virinchi(audio):
    keshava.say(audio)
    print("virinchi - ", audio)
    keshava.runAndWait()

def mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4)
    try:
        print("Recognizing...")
        micin = r.recognize_google(audio, language='en-in')
        print("user said:", micin)
        return micin.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "none"
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "none"

def updatetime():
    hour = int(datetime.datetime.now().hour)
    ct = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        virinchi("good morning, it's " + ct)
    elif hour >= 12 and hour <= 18:
        virinchi("good afternoon, it's " + ct)
    else:
        virinchi("good evening, it's " + ct)

def songs():
    virinchi("You are now in the entertainment zone. Which type of song do you prefer to listen to?")
    while True:
        micin = mic()
        if "hindi" in micin:
            kit.playonyt("Hit hindi songs")
        elif "old" in micin:
            kit.playonyt("Evergreen old songs")
        elif "english" in micin:
            kit.playonyt("best English hit songs")
        elif "punjabi" in micin:
            kit.playonyt("best punjabi hits")
        else:
            virinchi("Sorry, I am currently not developed to perform this action")
            break

def suffer():
    virinchi("Fasten Your seat belt and tell me your browser")
    while True:
        micin = mic()
        if "chrome" in micin:
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        elif "msedge" in micin:
            npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(npath)
        else:
            break

def main():
    while True:
        micin = mic()
        if "exit" in micin or "stop listening" in micin:
            break
        elif "open notepad" in micin:
            npath = "C:\\Windows\\system32\\notepad.exe"
            virinchi('opening notepad')
            os.startfile(npath)
        # Add other functionality here
    virinchi("Exiting main loop")

main ();
