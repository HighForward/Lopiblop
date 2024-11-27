import time

import pyautogui
import cv2
import numpy as np
from template import Template, updateScreenshot
from keyEvents import press_key, release_key, SPELL_KEY

class Slot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blop = None
        self.double = False

    def performClick(self):
        pyautogui.mouseDown(self.x, self.y)
        pyautogui.mouseUp(self.x, self.y)
        pyautogui.mouseDown(self.x, self.y)
        pyautogui.mouseUp(self.x, self.y)
        time.sleep(0.05)
        pyautogui.mouseDown(self.x + 60, self.y)
        pyautogui.mouseDown(self.x, self.y)


    def setBlop(self, imgs):
        start = time.time()
        self.performClick()

        screenshot_bgr, _ = updateScreenshot()

        tmpMax = 0

        for blop in imgs:
            result = cv2.matchTemplate(screenshot_bgr, blop.img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val > tmpMax:
                self.blop = blop
                tmpMax = max_val

        print("Found: ", self.blop.name, "in", time.time() - start)