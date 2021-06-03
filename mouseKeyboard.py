# imports

import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput import keyboard, mouse


# vars
x = 0
y = 0


# create an instance of the mouse controller
mController = pynput.mouse.Controller()

# create an instance of the keyboard controller
kController = pynput.mouse.Controller()

# moving the mouse
def on_release(key):
    global x, y
    if key == keyboard.Key.up:
        x = 0
        y = -10
        print("up pressed")
        mController.move(x, y)
    if key == keyboard.Key.down:
        x = 0
        y = 10
        print("down pressed")
        mController.move(x, y)
    if key == keyboard.Key.left:
        x = -10
        y = 0
        print("left pressed")
        mController.move(x, y)
    if key == keyboard.Key.right:
        x = 10
        y = 0
        print("right pressed")
        mController.move(x, y)
    if key == keyboard.Key.esc:
        listener.stop()
    if key == pynput.keyboard.KeyCode(char="q"):
        kController.click(Button.left)

# listening... in a non-blocking fashion:
listener = keyboard.Listener(on_release=on_release)
listener.start()
