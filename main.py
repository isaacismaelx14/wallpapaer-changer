import darkdetect
import ctypes
import os
import time

lastState = None;

def changeWallpaper(theme):
    path = os.path.dirname(os.path.abspath(__file__))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{path}\\assets\\{theme}.png", 0)

changeWallpaper(darkdetect.theme())

while True:
    currentState = darkdetect.theme()
    if(lastState != currentState):
        print("Changing wallpaper")
        changeWallpaper(currentState)
        lastState = currentState
    time.sleep(2);