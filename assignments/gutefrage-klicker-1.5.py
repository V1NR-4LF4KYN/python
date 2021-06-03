# python3

'''
Hi RidingGirl228.
EragonSaphira17 hier. Dieses Programm lässt dich eine beliebige Anzahl von Klicks mit nur
einem manuellem Klick von dir machen.
Die Anzahl der gemachten Klicks lässt sich von dir mit den "Plus" -und "Minus" -Tasten ändern.
Die Anzahl wird dann im Terminal (solltest du es offen haben) angezeigt und auch in einem
kleinem von dir verschiebbaren Fenster.


Das Programm lässt sich mit "ESC" beenden und mit "q" kannst du umschalten, ob es gerade läuft oder nicht.


NOTES: Fenster fehlt noch. Und anstelle zu klicken musst du "e" drücken.

Author: EragonSaphira17
Version: 1.5

'''
# imports
import time
import threading
import pynput
from tkinter import *

def update():
    try:
        import os

        os.system("pip install pynput")
        os.system("pip3 install pynput")
    except:
        print("Error occurred")
    finally:
        print("Finished")
    
# vars
delay = 0.15 # die Zeit zwischen den Klicks in Sekunden. Ich dachte erstmal 0.15 Sekunden wären realistisch.
button = pynput.mouse.Button.left
start_stop_key = pynput.keyboard.KeyCode(char='e') # Der Knopf zum Schießen
exit_key = pynput.keyboard.Key.esc


class ClickMouse(threading.Thread):
    ''' Create a class that extends threading.Thread that will allow us to control the mouse clicks '''
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.KLICKS = 1
        self.clickCounter = 0
        self.darfKlicken = True
        self.programmAktiviert = True
    
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
                print("Clicked times {0}".format(self.clickCounter), '\n')
            time.sleep(0.1)
        if self.clickCounter >= self.KLICKS:
            self.stop_clicking()
            self.clickCounter = 0
            print(self.clickCounter)


# Funktion für das Fenster
def showWindow(obj):
    top = Tk()
    # Ein Tkinter-Text-Widget.
    w = Text(top)
    w.insert(INSERT, obj.KLICKS + 1)
    w.pack()
    
    top.mainloop()


# create an instance of the mouse controller
mouse = pynput.mouse.Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key and click_thread.programmAktiviert == True:
        if click_thread.running:
            click_thread.stop_clicking()
            click_thread.clickCounter = 0
            click_thread.running = True
        else:
            click_thread.start_clicking()
            
    if key == exit_key:
        click_thread.exit()
        listener.stop()

    # Hier folgt die für dich wichtige Sache. Hier wird jetzt die Anzahl der Klicks verändert wenn "+" oder "-" gedrückt werden.
    if key == pynput.keyboard.KeyCode(char="+") and click_thread.programmAktiviert == True:
        click_thread.clickCounter += 1 #damit ein weiterer Klick verhindert wird
        print('Plus gedrückt...')
        click_thread.KLICKS += 1 # erhöhe KLICKS (Anzahl der Klicks)
        print('Anzahl der Klicks: {0}'.format(click_thread.KLICKS + 1), '\n')
        
        
    if key == pynput.keyboard.KeyCode(char="-") and click_thread.KLICKS > 0 and click_thread.programmAktiviert == True:
        print('Minus gedrückt...')
        click_thread.KLICKS -= 1 # verkleiner KLICKS (Anzahl der Klicks)
        print('Anzahl der Klicks: {0}'.format(click_thread.KLICKS + 1), '\n')
               
    
    # Hiermit aktivierst und deaktivierst du das Programm
    if key == pynput.keyboard.KeyCode(char="q"): # der knopf zum wechseln von aktiv und inaktiv des Programms
        if click_thread.programmAktiviert == True:
            click_thread.programmAktiviert = False
            print('Programm deaktiviert. \n')
        elif click_thread.programmAktiviert == False:
            click_thread.programmAktiviert = True
            print('Programm aktiviert. \n')


    
    
# with pynput.keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

# Auf folgende Art und Weise blockt der Listener nicht ab und das Fenster kann angezeigt werden
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

#showWindow(click_thread)

'''
Bestehende Probleme:
    - Das Fenster besteht zwar, jedoch aktualisiert es seinen Inhalt nicht.
    - Inputs zum Klicken können noch nicht mit der Maus gegeben werden. Derzeit wird 'e' verwendet.
'''






