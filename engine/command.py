from imaplib import Commands
import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    text = str(text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(2)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
        

    try:
      print("Recognizing...")
      eel.DisplayMessage("Recognizing...")
      query = r.recognize_google(audio, language="en-US")
      print(f"User said: {query}")
      eel.DisplayMessage(query)
    
      

    except Exception as e:
        print("Sorry, I didn't catch that.")
        return ""

    return query.lower()
  
@eel.expose
def allCommands():
  query = takecommand()
  print(query)
  if "open" in query:
    from engine.features import openCommand
    openCommand(query)
  elif "play" in query and "on youtube" in query:
    from engine.features import PlayYoutube
    PlayYoutube(query)

  else:
    print("Command not recognized.")
   
  eel.ShowHood()
