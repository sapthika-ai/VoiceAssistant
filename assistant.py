import speech_recognition as sr
import pyttsx3
import tkinter as tk
import threading
import datetime
import webbrowser


engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

running = False

def process_command(command):
    command = command.lower()
    print("User said:", command)

    if "hello" in command:
        speak("Hello! I am your assistant. How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%A %d %B %Y")
        speak(f"Today is {date}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "your name" in command:
        speak("I am your personal voice assistant")

    elif "stop" in command:
        speak("Stopping assistant")
        stop_assistant()

    else:
        speak("Sorry, I did not understand that command")


def listen():
    global running
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while running:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            process_command(command)

        except sr.UnknownValueError:
            speak("I could not understand that")

        except Exception as e:
            print("Error:", e)


def start_assistant():
    global running
    if not running:
        running = True
        speak("Assistant started")
        threading.Thread(target=listen, daemon=True).start()


def stop_assistant():
    global running
    running = False
    speak("Assistant stopped")


window = tk.Tk()
window.title("AI Voice Assistant - Major Project")
window.geometry("400x300")
window.config(bg="#1e1e1e")

title = tk.Label(window, text="VOICE ASSISTANT",
                 font=("Arial", 18, "bold"),
                 fg="white", bg="#1e1e1e")
title.pack(pady=20)

start_btn = tk.Button(window,
                      text="START",
                      font=("Arial", 14),
                      bg="green",
                      fg="white",
                      width=15,
                      command=start_assistant)
start_btn.pack(pady=10)

stop_btn = tk.Button(window,
                     text="STOP",
                     font=("Arial", 14),
                     bg="red",
                     fg="white",
                     width=15,
                     command=stop_assistant)
stop_btn.pack(pady=10)

info = tk.Label(window,
                text="Say: hello, time, date, open youtube",
                fg="white",
                bg="#1e1e1e")
info.pack(pady=20)

window.mainloop()
