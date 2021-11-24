import pyautogui as auto
#import sys

try:
    while True:
        x, y = auto.position()
        auto.moveTo(x+100, y+100, 5)
        auto.moveTo(x, y, 4)
except KeyboardInterrupt:
    print("done")
