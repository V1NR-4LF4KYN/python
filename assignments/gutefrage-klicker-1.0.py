# python3

'''
Hi RidingGirl228.
EragonSaphira17 hier. Dieses Programm lässt dich eine beliebige Anzahl von Klicks mit nur
einem manuellem Klick von dir machen.
Die Anzahl der gemachten Klicks lässt sich von dir mit den "Plus" -und "Minus" -Tasten ändern.
Die Anzahl wird dann im Terminal (solltest du es offen haben) angezeigt und auch in einem
kleinem von dir verschiebbaren Fenster.

Des Weiteren ist es dir möglich dieses Programm, oder sagen wir die Klicker-Funktion dieses Programmes
mithilfe der Taste "q" auszuschalten.

Ich würde dir empfehlen dir Thonny runterzuladen und das Programm so zu starten innerhalb von Thonny.


Author: EragonSaphira17
Version: 1.1

'''
# imports
import pynput
from pynput.keyboard import Key
from pynput import keyboard
from pynput import mouse
#import pyautogui



# installiere alle benötigten Libraries. Nur beim Erststart nötig. Danach kannst du diese kleine Sektion auskommentieren.
'''
try:
    print("Installiere nötige Libraries...")
    
    import os
    
    os.system("pip install pynput")
    os.system("pip install pyautogui")
    os.system("pip3 install pynput")
    os.system("pip3 install pyautogui")
except:
    print("Fehler beim Installieren der Libs. Ignoriere das.")
finally:
    print("Installieren der Libs fertig.\n\n")

#Bis hier kommentieren, wenn einmal gelaufen.
'''


# vars
KLICKS = 2 # die Anzahl der Klicks und ihre Standard-Einstellung
darfKlicken = True
programmAktiviert = True



# funcs

def on_release(key):
    ''' Keyboard Funktionen '''        
    global KLICKS, programmAktiviert
    
    # Hier folgt die für dich wichtige Sache. Hier wird jetzt die Anzahl der Klicks verändert wenn "+" oder "-" gedrückt werden.
    if key == pynput.keyboard.KeyCode(char="+") and programmAktiviert == True:
        print('Plus gedrückt...')
        KLICKS += 1 # erhöhe KLICKS (Anzahl der Klicks)
        print('Anzahl der Klicks: {0}'.format(KLICKS), '\n')

    if key == pynput.keyboard.KeyCode(char="-") and KLICKS > 0 and programmAktiviert == True:
        print('Minus gedrückt...')
        KLICKS -= 1 # verkleiner KLICKS (Anzahl der Klicks)
        print('Anzahl der Klicks: {0}'.format(KLICKS), '\n')
    
    # Hiermit aktivierst und deaktivierst du das Programm
    if key == pynput.keyboard.KeyCode(char="q"):
        if programmAktiviert == True:
            programmAktiviert = False
            print('Programm deaktiviert. \n')
        elif programmAktiviert == False:
            print('Programm aktiviert. \n')



mouse = pynput.mouse.Controller()

def on_click(x, y, button, pressed):
    global KLICKS, darfKlicken, programmAktiviert

    if pressed and darfKlicken == True and programmAktiviert == True:
        print('started')


    if not pressed and darfKlicken == True and programmAktiviert == True:
        print('finished')
        darfKlicken = False
        pyautogui.click(clicks=2)

#     if darfKlicken == False:
#         darfKlicken = True


''' LISTENERS (Zur Erklärung: Diese registrieren Maus-Klicks und Tastenanschläge für dich) '''    
# Collect keyboard events until released
listener = keyboard.Listener(on_release=on_release)
listener.start()

listener2 = pynput.mouse.Listener(on_click=on_click)
listener2.start()

