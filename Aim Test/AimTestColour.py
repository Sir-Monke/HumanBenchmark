import mss
import pyautogui
import numpy as np
import cv2

top_left = (2100, 170)
bottom_left = (2100, 700)
top_right = (3100, 170)
bottom_right = (3100, 700)

color_to_find = (232, 195, 149)

clicks_made = 0
total_clicks = 31
start = True

while start:
    while clicks_made != total_clicks:
        with mss.mss() as sct:
            monitor = {
                "top": top_left[1],
                "left": top_left[0],
                "width": top_right[0] - top_left[0],
                "height": bottom_left[1] - top_left[1]
            }
            screenshot = np.array(sct.grab(monitor))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
            pixel_matches = np.all(screenshot == color_to_find, axis=2)
            y_coords, x_coords = np.where(pixel_matches)
            if len(y_coords) > 0:
                x, y = x_coords[0] + top_left[0], y_coords[0] + top_left[1]
                pyautogui.click(x + 5, y + 5)
                clicks_made += 1
    else:
        start = False
        if input("Would You Like To Go Again?") == "y":
            clicks_made = 0
            start = True
        else:
            break
