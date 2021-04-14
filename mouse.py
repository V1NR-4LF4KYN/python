import pyautogui as p

try:
    print(p.position())
    p.move(50, 50)
except:
    print("aborted")
