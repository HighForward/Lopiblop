import pygetwindow as gw
import pyautogui
import numpy as np
import cv2
import os
import time
import keyboard
import sys


from grid import initGrid
from template import Template, updateScreenshot, LoadBlopImages
from pnj import startLopiblop
from slot import Slot
from utils import getDoubleIndex
from keyEvents import press_key, release_key, SPELL_KEY

windows = gw.getWindowsWithTitle('Qxqx')  # Replace 'Window Title' with the actual window title

grid = []
initGrid(grid)

def WaitUntilSpellReady(nospell):
    press_key(SPELL_KEY)
    release_key(SPELL_KEY)

    time.sleep(0.1)
    while True:
        screenshot_bgr, screenshot_gray = updateScreenshot()
        val = nospell.matchTemplateGray(screenshot_gray)
        if val is True:
            print('Spell Ready')
            break


if windows:
    window = windows[0]
    window.resizeTo(1600, 1000)
    window.moveTo(0, 0)
    window.activate()

    time.sleep(1)

    startLopiblop()
    imgs = LoadBlopImages()

    nospell = Template("pnj", "nospell.png")
    while True:

        currTurn = 0

        for i, _ in enumerate(grid):

            if keyboard.is_pressed('esc'):
                print("Exit")
                sys.exit()

            pyautogui.moveTo(grid[i].x, grid[i].y)
            WaitUntilSpellReady(nospell)

            if grid[i].blop is None:
                grid[i].setBlop(imgs)

            currTurn = currTurn + 1

            if currTurn == 2 and grid[i].blop.name == grid[i - 1].blop.name:
                currTurn = 0
                continue

            iDouble = getDoubleIndex(grid, i)
            if iDouble > -1:
                print("Double Found", i, iDouble)

                WaitUntilSpellReady(nospell)

                if currTurn == 1:
                    grid[iDouble].performClick()
                else:
                    pyautogui.moveTo(grid[iDouble].x, grid[iDouble].y)
                    WaitUntilSpellReady(nospell)
                    grid[iDouble].performClick()
                    pyautogui.moveTo(grid[iDouble].x, grid[iDouble].y)
                    WaitUntilSpellReady(nospell)
                    grid[i].performClick()
                currTurn = 0

        if currTurn == 2:
            currTurn = 0

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Window not found!")