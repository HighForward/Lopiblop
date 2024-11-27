import pygetwindow as gw
import pyautogui
import numpy as np
import cv2
import os
import time

from template import Template, updateScreenshot
from slot import Slot
from keyEvents import press_key, release_key

windows = gw.getWindowsWithTitle('Qxqx')  # Replace 'Window Title' with the actual window title

def LoadBlopImages():
    images = []
    for filename in os.listdir("blops_img"):
        images.append(Template("blops_img", filename))
    return images

def startLopiblop():
    screen = updateScreenshot()
    pnj = Template("pnj", "lopiblop_pnj.png")
    pnj.matchTemplate(screen)
    pyautogui.mouseDown(pnj.x, pnj.y)
    pyautogui.mouseUp(pnj.x, pnj.y)
    print("lopiblop Clicked")
    time.sleep(1)

    screen = updateScreenshot()
    dialog = Template("pnj", "play.png")
    dialog.matchTemplate(screen)
    pyautogui.mouseDown(dialog.x, dialog.y)
    pyautogui.mouseUp(dialog.x, dialog.y)
    print("play dialog Clicked")
    time.sleep(1)

    screen = updateScreenshot()
    ready = Template("pnj", "ready.png")
    ready.matchTemplate(screen)
    pyautogui.mouseDown(ready.x, ready.y)
    pyautogui.mouseUp(ready.x, ready.y)
    print("ready clicked")
    time.sleep(1)

def nextTurn():
    screen = updateScreenshot()
    next = Template("pnj", "next.png")
    next.matchTemplate(screen)
    pyautogui.mouseDown(next.x, next.y)
    pyautogui.mouseUp(next.x, next.y)
    pyautogui.mouseDown(next.x, next.y)
    pyautogui.mouseUp(next.x, next.y)
    print("next turn clicked")

grid = []
grid.append(Slot(860, 320))
grid.append(Slot(945, 360))
grid.append(Slot(1028, 400))
grid.append(Slot(1110, 440))
grid.append(Slot(1195, 480))
grid.append(Slot(1275, 520))

grid.append(Slot(780, 360))
grid.append(Slot(860, 400))
grid.append(Slot(946, 440))
grid.append(Slot(1028, 480))
grid.append(Slot(1110, 520))
grid.append(Slot(1192, 560))

grid.append(Slot(700, 400))
grid.append(Slot(780, 440))
grid.append(Slot(860, 480))
grid.append(Slot(945, 520))
grid.append(Slot(1026, 560))
grid.append(Slot(1110, 600))

grid.append(Slot(612, 440))
grid.append(Slot(700, 480))
grid.append(Slot(780, 520))
grid.append(Slot(860, 560))
grid.append(Slot(945, 600))
grid.append(Slot(1026, 640))


def getDoubleIndex(i):
    tmp = 0
    while tmp < i:
        if grid[tmp].blop and grid[i].blop and grid[tmp].blop.name == grid[i].blop.name:
            return tmp
        tmp += 1
    return -1

if windows:
    window = windows[0]
    window.resizeTo(1600, 1000)
    window.moveTo(0, 0)
    window.activate()

    time.sleep(1)

    startLopiblop()
    imgs = LoadBlopImages()

    run = True
    while run:

        currTurn = 0
        i = 0
        while i < len(grid):

            if grid[i].double == False and grid[i].blop is None:
                pyautogui.moveTo(grid[i].x, grid[i].y)
                grid[i].setBlop(imgs)
                time.sleep(0.2)

                currTurn = currTurn + 1

                if currTurn == 2 and grid[i].blop.name == grid[i - 1].blop.name:
                    currTurn = 0
                    time.sleep(4)
                    continue

                iDouble = getDoubleIndex(i)


                if iDouble > -1:
                    print("Double Found -", "current: ", i, "Double: ", iDouble, " - Turn: ", currTurn)
                    if currTurn == 1:
                        grid[iDouble].performClick()
                    else:
                        time.sleep(3.5)
                        grid[i].performClick()
                        time.sleep(0.2)
                        grid[iDouble].performClick()

                    grid[i].double = True
                    grid[iDouble].double = True
                    time.sleep(3.5)
                    currTurn = 0
                continue

            if currTurn == 2:
                currTurn = 0
                time.sleep(3.5)

            i = i + 1



    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Window not found!")