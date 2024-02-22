import os
import pyttsx3 as p
import openai
from api_key import API_KEY
import time
import datetime
import subprocess
import speech_recognition as sr
import pyaudio
import webbrowser
# set voice
engine = p.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)
engine.setProperty('rate', 200)

# start talk function
def talk(text):
    volume = 0.9
    delay = 0.01
    engine.say(text)
    engine.runAndWait()
    time.sleep(delay)

def time_count():
    hours = datetime.datetime.now().hour
    if 0 <= hours < 12:
        talk("Good morning sir, I am your Voice assistant. How are you?")
    elif 12 <= hours < 16:
        talk("Good afternoon sir, I am your Voice assistant. How are you?")
    else:
        talk("Good evening sir, I am your Voice assistant. How are you?")
time_count()
# speech to text
def speak_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...listening")
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.0)
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=10)
        try:
            # Recognize speech using Google's Speech Recognition
            print("recognizing...")
            text = r.recognize_google(audio)
            print(text)
            return text.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# the main execution file
if __name__ == "__main__":
    while True:
        command = speak_command()
        if command is None :
            talk(" i havent got your message . Please try again")  
            speak_command()   
        elif 'fine' in command:
            talk(" I'm glad you are fine. How can i help you ?")
            speak_command()

        elif 'open youtube' in command:
            try:
                os.system("brave-browser https://www.youtube.com")
                break  # Break out of the loop after opening YouTube
            except FileNotFoundError:
                print("Brave browser not found. Make sure it is installed and in your PATH.")
        elif 'open brave' in command:
            try:
                os.system("brave-browser")
                break  # Break out of the loop after opening YouTube
            except FileNotFoundError:
                print("Brave browser not found. Make sure it is installed and in your PATH.")
        elif 'open folder' in command:
            try:
                os.system("thunar")
                break  # Break out of the loop after opening YouTube
            except FileNotFoundError:
                print("Brave browser not found. Make sure it is installed and in your PATH.")        
        elif 'play me a song' in command:
            try:
                talk("Sure! What song would you like me to play?")
                song_name = speak_command()
                search_query = f"{song_name}"
                talk(f"Searching for {song_name} on YouTube.")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                break  # Break out of the loop after opening the search results
            except Exception as e:
                print(f"An error occurred: {e}")
        elif "oprn thunar" in command:
            try:
                os.system('thunar') 
                break;
            except Exception as e:
                print(f"error occured while opening {e}")

        else:
            speak_command()        
