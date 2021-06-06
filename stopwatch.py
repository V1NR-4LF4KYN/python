# Stopwatch program

import time
import pyautogui

x = time.time()

time.sleep(3)

y = time.time()

z = y-x
print(x, y)
print(round(z))