import os
import cv2
import numpy as np
import pyautogui


def updateScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    # screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)
    return screenshot_bgr

class Template:

    def __init__(self, folder, name):
        self.x = None
        self.y = None
        self.folder = folder
        self.name = name

        img = cv2.imread(os.path.join(folder, name))
        if img is not None:
            h, w, _ = img.shape
            self.img = img
            self.height = h
            self.width = w

    def matchTemplate(self, screenshot_bgr):
        result = cv2.matchTemplate(screenshot_bgr, self.img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.9:
            top_left = max_loc
            self.x = top_left[0] + (self.width / 2)
            self.y = top_left[1] + (self.height / 2)