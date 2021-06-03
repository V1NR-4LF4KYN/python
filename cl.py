'''
This program will click once wherever the mouse is right now
Exactly 1 Second after executing it

'''

# imports
import pyautogui as p
from time import sleep


# funcs
def c():
    ''' will wait and click'''
    sleep(1)
    p.click()



# mainloop
def main():
    c()

# calling main-func
main()