import speech_recognition as sr
import pyttsx3 as p  # for text-to-speech Conversion
from sel import infow
import subprocess
from weather import Weather
from tkinter import *
import sys
import threading


engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

r = sr.Recognizer()


screen = Tk()
screen.title("Voice Assistant")
screen.config(padx=50, pady=30)

canvas = Canvas(width=400, height=400)
t_image = PhotoImage(file="V_pic.png")
canvas.create_image(200, 150, image=t_image)
action_text = canvas.create_text(
    200, 300, text="Welcome...", font=("Courier", 15, "bold"))
canvas.grid(row=1, column=1)

listening_thread = None


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening.....")
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("Sorry, Sir.Please repeat again.")
            return "Try again"
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")
            return "Sorry, there was an issue with the service."


def greeting():
    speak("Hello Sir. I am Cassie. How May I help you.")


def handle_command(text):
    if "search" and "wikipedia" in text.lower():
        speak("Please tell me the topic sir")
        query = listen()
        assist = infow()
        assist.get_info(query)

    elif "video" and "youtube" in text.lower():
        speak("Please tell me the name of the song you want to play")
        query = listen()
        speak("Enjoy the song")
        assist = infow()
        assist.play_video(query)

    elif "open" and "excel" in text.lower():
        speak("Opening Excel")
        subprocess.Popen(
            "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")

    elif "open" and "word" in text.lower():
        speak("Opening Word")
        subprocess.Popen(
            "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")

    elif "open" and "powerpoint" in text.lower():
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
        try:
            speak("Have a good day")
            screen.quit()  # Stop the Tkinter main loop
            screen.destroy()  # Close the window
            sys.exit()
        except RuntimeError:
            pass

    elif "how" and "are" and "you" in text.lower():
        speak("I am fine sir.")


def update_text():
    global listening_thread
    # Check if the listening thread is already running to prevent interruption of already running thread and preventing runtime error while exiting the window.
    if listening_thread and listening_thread.is_alive():
        screen.after(1000, update_text)
        return

    def threaded_listen_and_speak():
        canvas.itemconfig(action_text, text="Listening...")
        text = listen()
        canvas.itemconfig(action_text, text=f"{text.capitalize()}")
        handle_command(text)
        listening_thread = None

    listening_thread = threading.Thread(target=threaded_listen_and_speak)
    listening_thread.start()
    screen.after(1000, update_text)


screen.after(1000, greeting)
screen.after(2000, update_text)

screen.mainloop()
