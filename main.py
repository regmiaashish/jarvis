import os
import eel 
from engine.features import playAssistantSound
from engine.command import *
playAssistantSound()



eel.init('www')

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, block=True, host='localhost', port=8000, size=(800, 600))