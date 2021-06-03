#python3

'''
I Need This Program to set the High Score on "How Long Can You Hold The Button?"
And It Actually Works :D
Tried the "mouse"-module before and it didn't work on my Rasperry Pi

'''

#imports 
import pyautogui
import time 

# funcs
def waitForWindowSwitch():
    time.sleep(5)

def holdMouse(seconds): # time in seconds
    pyautogui.mouseDown(button='left')
    time.sleep(seconds)
    pyautogui.mouseUp()

# mainloop
def  main():
    # give user some time to switch to whatever is going to be clicked
    waitForWindowSwitch()
    
    #acually hold the mouse
    holdMouse(1)


#call main
main()