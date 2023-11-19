import cv2
import numpy as np
import pyautogui
import mss

top_left = (2100, 170)
bottom_left = (2100, 700)
top_right = (3200, 170)
bottom_right = (3100, 700)

clicks_made = 0
total_clicks = 31
start = True

image_dir = "DIR"

while start:
    with mss.mss() as sct:
        while clicks_made != total_clicks:
            monitor = {"top": top_left[1], "left": top_left[0], "width": bottom_right[0] - top_left[0], "height": bottom_right[1] - top_left[1]}
            screenshot = np.array(sct.grab(monitor))
            image_to_search = cv2.imread(image_dir)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
            result = cv2.matchTemplate(screenshot, image_to_search, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            top_left_match = max_loc
            if max_val > 0:
                click_x, click_y = top_left_match
                pyautogui.click(top_left[0] + click_x, top_left[1] + click_y)
                clicks_made += 1
        else:
            start = False
            if input("Would You Like To Go Again?") == "y":
                clicks_made = 0
                start = True
            else:
                break
