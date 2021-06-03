#python3

import random

again=True
min=1
max=6


while again==True:
    number = random.randint(min,max)
    print("The number is: ", number)
    userInput = input("Do you want to roll the dice again? Type \"y\" or \"n\"\n")
    if userInput == "y":
        again=True
    elif userInput == "n":
        print("Okay, bye bye...")
        again=False
        #exit()
    else:
        print("Error... Program ending...")
        again=False
        #exit()

userContinue = input("Do you want to exit the shell? \"y\" or \"n\"? \n")

if userContinue == "y":
    exit()

