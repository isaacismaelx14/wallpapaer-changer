import darkdetect
import ctypes
import os
import time

lastState = None;

def changeWallpaper(theme):
    path = os.path.dirname(os.path.abspath(__file__))
    fileType = ".png"  # change this is your file is different to .png

    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, f"{path}\\assets\\{theme}{fileType}", 0)

# darkdetect.theme() return -> "Dark" or "Light"
changeWallpaper(darkdetect.theme())

while True:
    currentState = darkdetect.theme()
    if(lastState != currentState):
        print("Changing wallpaper")
        changeWallpaper(currentState)
        lastState = currentState
    time.sleep(2);