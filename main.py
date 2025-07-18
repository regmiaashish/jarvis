import os
import eel # type: ignore

eel.init('www')

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, block=True, host='localhost', port=8000, size=(800, 600))