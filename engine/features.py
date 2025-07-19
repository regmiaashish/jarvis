from playsound  import  playsound
import eel
from engine.config import ASSISTANT_NAME
import os 
import webbrowser
import sqlite3
from engine.command import speak
import pywhatkit as kit
from engine.helper import extract_yt_term



@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
      speak("Opening " + query)
      os.system('start ' + query)
    else:
      speak("Please specify what you want to open.")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on YouTube")
    kit.playonyt(search_term)
