# python3

'''
Hi RidingGirl228.
EragonSaphira17 hier. Dieses Programm lässt dich eine beliebige Anzahl von Klicks mit nur
einem manuellem Klick von dir machen.
Die Anzahl der gemachten Klicks lässt sich von dir mit den "Plus" -und "Minus" -Tasten ändern.
Die Anzahl wird dann im Terminal (solltest du es offen haben) angezeigt und auch in einem
kleinem von dir verschiebbaren Fenster.


Ich würde dir empfehlen dir Thonny runterzuladen und das Programm so zu starten innerhalb von Thonny.


Author: EragonSaphira17
Version: 1.3

'''
# imports
import time
import threading
import pynput


# vars
delay = 0.15
button = pynput.mouse.Button.left
start_stop_key = pynput.keyboard.KeyCode(char="e")
exit_key = pynput.keyboard.Key.esce



class ClickMouse(threading.Thread):
    ''' Create a class that extends threading.Thread that will allow us to control the mouse clicks '''
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        # counter for clicks
        self.KLICKS = 2
        self.clickCounter = 0
    
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
    
    def run(self):
        while self.program_running:
            while self.running and self.clickCounter <= self.KLICKS:
                mouse.click(self.button)
                time.sleep(self.delay)
                self.clickCounter += 1
                print("Clicked times {0}".format(self.clickCounter))
            time.sleep(0.1)
        if self.clickCounter >= self.KLICKS:
            self.stop_clicking()
            self.clickCounter = 0
            print(self.clickCounter)
            
# create an instance of the mouse controller
mouse = pynput.mouse.Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            click_thread.clickCounter = 0
        else:
            click_thread.start_clicking()
    if key == exit_key:
        click_thread.exit()
        listener.stop()
    
    
    
    
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()



