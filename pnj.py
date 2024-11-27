import pyautogui
import time
from keyEvents import press_key, release_key
from template import Template, updateScreenshot


def startLopiblop():
    # screen, _ = updateScreenshot()
    # pnj = Template("pnj", "lopiblop_pnj.png")
    # pnj.matchTemplate(screen)
    pyautogui.mouseDown(480, 510)
    pyautogui.mouseUp(480, 510)
    pyautogui.mouseDown(480, 510)
    pyautogui.mouseUp(480, 510)
    time.sleep(1)

    # screen, _ = updateScreenshot()
    # dialog = Template("pnj", "play.png")
    # dialog.matchTemplate(screen)
    # pyautogui.mouseDown(dialog.x, dialog.y)
    # pyautogui.mouseUp(dialog.x, dialog.y)
    pyautogui.mouseDown(680, 570)
    pyautogui.mouseUp(680, 570)
    pyautogui.mouseDown(680, 570)
    pyautogui.mouseUp(680, 570)
    time.sleep(1)


    press_key(0x3B)
    release_key(0x3B)
    # screen, _ = updateScreenshot()
    # ready = Template("pnj", "ready.png")
    # ready.matchTemplate(screen)
    # pyautogui.mouseDown(ready.x, ready.y)
    # pyautogui.mouseUp(ready.x, ready.y)
    time.sleep(1)

    print("Fight Started")

def nextTurn():
    screen, _ = updateScreenshot()
    next = Template("pnj", "next.png")
    next.matchTemplate(screen)
    pyautogui.mouseDown(next.x, next.y)
    pyautogui.mouseUp(next.x, next.y)
    pyautogui.mouseDown(next.x, next.y)
    pyautogui.mouseUp(next.x, next.y)
    print("Next Turn")