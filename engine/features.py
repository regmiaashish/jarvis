from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
import webbrowser
import sqlite3
from engine.command import speak
import pywhatkit as kit
from engine.helper import extract_yt_term
import time

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    if app_name := query:
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if results:
                speak("Opening " + app_name)
                os.startfile(results[0][0])
            else:
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()
                
                if results:
                    speak("Opening " + app_name)
                    webbrowser.open(results[0][0])
                else:
                    # Try direct execution
                    speak("Opening " + app_name)
                    try:
                        os.system(f'start {app_name}')
                    except Exception as e:
                        print(f"System launch failed: {e}")
                        speak("App not found.")
        except Exception as e:
            print(f"Database error: {e}")
            speak("Something went wrong while accessing commands.")
    else:
        speak("I didn't catch the app name.")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on YouTube")
    try:
        kit.playonyt(search_term)
    except Exception as e:
        print(f"YouTube error: {e}")
        speak("Something went wrong while opening YouTube.")
