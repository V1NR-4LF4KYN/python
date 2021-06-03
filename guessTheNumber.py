#python3

# imports
import random

# vars
min = 1
max = 10
randNum = 0
isGuessing = True

#funcs
def greet():
    print("Welcome!\n")
    

def getRandomNumber(): # assigning a random value to randNum
    global randNum
    global isGuessing
    
    randNum = random.randint(min, max)
    #print(randNum)


def guessPlay(): # actual game-code
    global isGuessing
    
    print("Guess the number between ", min, " and ", max, " : ")
    playerValue = int(input(""))
    
    if playerValue < randNum:
        print("\nToo low... Try again\n")
    elif playerValue > randNum:
        print("\nToo high... Try again\n")
    else:
        isGuessing = False
        print("\nCongrats! You Won!\n")
    

#main-loop
def main():
    global isGuessing
    greet()
    getRandomNumber()
    
    while isGuessing:
        guessPlay()
    
    #exit()

#calling main func
main()