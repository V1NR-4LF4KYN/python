#python3

import random

#randNum = 0
class Random:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.randNum = randNum = 0
        self.isGuessing = isGuessing = True
        self.playerValue = playerValue = 0
    
    def getRandomNumber(self): # getting a random number itself
        self.randNum = random.randint(self.min, self.max)
    
    def guessPlay(self): # actual game-code
        print("Guess the number between ", self.min, " and ", self.max, " : ")
        self.playerValue = int(input(""))
        
        if self.playerValue < self.randNum:
            print("\nToo low... Try again\n")
        elif self.playerValue > self.randNum:
            print("\nToo high... Try again\n")
        else:
            self.isGuessing = False
            print("\nCongrats! You Won!\n")
    


r = Random(1, 10) # creating instance of class

# playing game 
r.getRandomNumber()
while r.isGuessing:
    r.guessPlay()







