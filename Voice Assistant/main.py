import speech_recognition as sr
import pyttsx3 as p
from sel import infow
import subprocess
from weather import Weather
import sys


engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening.....")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        return text


speak("Hello Sir. I am Cassie. How May I help you.")

while True:
    try:
        text = listen()
        if "search" and "wikipedia" in text.lower():
            speak("Please tell me the topic sir")
            query = listen()
            assist = infow()
            assist.get_info(query)

        elif "video" and "youtube" in text.lower():
            speak("Please tell me the name of the song you want to play")
            query = listen()
            assist = infow()
            assist.play_video(query)

        elif "excel" in text.lower():
            speak("Opening Excel")
            subprocess.Popen(
                "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")

        elif "word" in text.lower():
            speak("Opening Word")
            subprocess.Popen(
                "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")

        elif "powerpoint" in text.lower():
            speak("Opening PowerPoint")
            subprocess.Popen(
                "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")

        elif "weather" in text.lower():
            speak("Providing weather details")
            w = Weather()
            data = w.get_weather()
            speak(f"It seems like {data['weather'][0]['description']}")
            speak(
                f"Temperature feels like {data['main']['feels_like']} Fahrenheit")
            speak(f"Wind speed is {data['wind']['speed']} km per hour")

        elif "exit" in text.lower():
            speak("Have a good day")
            sys.exit()

        elif ("what" and "about" and "you") or ("how" and "are" and "you") in text.lower():
            speak("I am also fine sir.")

        else:
            speak(
                "Sorry sir. I am unable to understand your request. Please give clear instructions.")

    except sr.exceptions.UnknownValueError as e:
        pass
