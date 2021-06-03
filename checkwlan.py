# checks wether the device is connected to the internet

import os

def x():
    if (os.system("ping google.com -c 1 ")) == 0:
        os.system("clear")
        print("Connected :)")
    else:
        os.system("clear")
        print("NOT Connected :(")

x()
