import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'vajra' in command:
                command = command.replace('vajra', '')
                print(command)
    except Exception as e:
        print("Error: " + str(e))
    return command

def run_vajra():
    command = take_command()
    if command:
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'tell me about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')

def on_click(event):
    threading.Thread(target=run_vajra).start()

# Set up the GUI
app = tk.Tk()
app.title("Vajra Voice Assistant")
app.geometry("400x300")

# Load the background image from a URL
image_url = "https://t3.ftcdn.net/jpg/04/91/09/72/360_F_491097264_CGuzXDvKPkKBTxUnX0Jg9k5rbinL3Xhv.jpg" # Replace with your image URL

try:
    response = requests.get(image_url)
    response.raise_for_status()  # Check if the request was successful
    bg_image = Image.open(BytesIO(response.content))
    bg_image = bg_image.resize((400, 300), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
except Exception as e:
    print(f"Failed to load image: {e}")
    bg_photo = None

# Create a label and add the background image
if bg_photo:
    bg_label = tk.Label(app, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.bind("<Button-1>", on_click)
else:
    app.configure(bg='lightgrey')  # Fallback background color
    app.bind("<Button-1>", on_click)

def start_listening_loop():
    threading.Thread(target=run_vajra).start()
    app.after(15000, start_listening_loop)

# Start the listening loop
start_listening_loop()

app.mainloop()
