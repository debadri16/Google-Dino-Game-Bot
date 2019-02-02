from PIL import ImageGrab, ImageOps
import pyautogui
import time
import keyboard
from numpy import *

class Co_ordinates():
    replayBtn = (960, 456)
    dinosaur = (582,514)
    #680,563

def restartGame():
    time.sleep(5)
    print('starting')
    pyautogui.click(Co_ordinates.replayBtn)
    print('end')

def pressSpace():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def imageGrab():
    box = (Co_ordinates.dinosaur[0]+680-582,Co_ordinates.dinosaur[1],Co_ordinates.dinosaur[0]+680-563+40,Co_ordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return(a.sum())

def main():
    while True:
        if imageGrab() != 2017:
            pressSpace()
            if keyboard.is_pressed('q'):
                break

restartGame()
main()
