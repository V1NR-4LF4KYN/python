# checks wether the device is connected to the internet
# rewritten to be oop

import os

class Checker:
    def __init__(self):
        pass


    def checkwlan(self):
        if (os.system("ping google.com -c 1 ")) == 0:
            os.system("clear")
            print("Connected :)")
        else:
            os.system("clear")
            print("NOT Connected :(")

c = Checker()
c.checkwlan()
