import os
import cv2
import numpy as np
import pyautogui

#640 - 900
#725 - 1000

def updateScreenshot(onlyBlop = False):

    screenshot = None
    if onlyBlop is False:
        screenshot = pyautogui.screenshot(region=(0, 0, 1600, 1000))
    else:
        screenshot = pyautogui.screenshot(region=(440, 800, 350, 200))
    screenshot_np = np.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)
    return screenshot_bgr, screenshot_gray


def LoadBlopImages():
    images = []
    for filename in os.listdir("blops_img"):
        images.append(Template("blops_img", filename))
    return images

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

    def matchTemplateGray(self, screenshot_gray):

        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(screenshot_gray, img, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= 0.9)

        for pt in zip(*locations[::-1]):  # Get (x, y) coordinates of matching areas
            return False
        return True