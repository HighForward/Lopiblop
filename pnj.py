import pyautogui
import time

from template import Template, updateScreenshot

def startLopiblop():
    screen, _ = updateScreenshot()
    pnj = Template("pnj", "lopiblop_pnj.png")
    pnj.matchTemplate(screen)
    pyautogui.mouseDown(pnj.x, pnj.y)
    pyautogui.mouseUp(pnj.x, pnj.y)
    time.sleep(1)

    screen, _ = updateScreenshot()
    dialog = Template("pnj", "play.png")
    dialog.matchTemplate(screen)
    pyautogui.mouseDown(dialog.x, dialog.y)
    pyautogui.mouseUp(dialog.x, dialog.y)
    time.sleep(1)

    screen, _ = updateScreenshot()
    ready = Template("pnj", "ready.png")
    ready.matchTemplate(screen)
    pyautogui.mouseDown(ready.x, ready.y)
    pyautogui.mouseUp(ready.x, ready.y)
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