'''
A Rock Paper Scissors-Game.

'''

### Logic ###
'''
Scissors Scissors 11 tie
Scissors Rock 12 loss
Scissors Paper 13 win

Rock Scissors 21 win
Rock Rock 22 tie
Rock Paper 23 loss

Paper Scissors 31 loss
Paper Rock 32 win
Paper Paper 33 tie
'''

# imports
import random

# funcs
# main-loop
def main():
    # vars
    playerChoice = 0
    aiChoice = 0
    
    # getting an aiChoice    
    aiChoice = random.randint(1,3)
    # print(aiChoice) # only for testing purposes
    
    # getting a playerChoice
    playerChoice = int(input("Enter a number between 1 and 3 --> 1 is Scissors, 2 is Rock, 3 is Paper\n: "))
    
    
    # Basically a Python Switch-Case-Statement
    # first Layer is for Determining the Player's Choice
    # The Second Layer is for Determining the AI's Choice
    
    # first case
    if playerChoice == 1:
        print("Your choice: Scissors")
        if aiChoice == 1: # ai 1
            print("AI's choice: Scissors")
            print("Tie!")
        elif aiChoice == 2: # ai 2
            print("AI's choice: Rock")
            print("The AI Won!")
        elif aiChoice == 3: # ai 3
            print("AI's choice: Paper")
            print("You Won!")
    # second case
    elif playerChoice == 2:
        print("Your choice: Rock")
        if aiChoice == 1: # ai 1
            print("AI's choice: Scissors")
            print("You Won!")
        elif aiChoice == 2: # ai 2
            print("AI's choice: Rock")
            print("Tie!")
        elif aiChoice == 3: # ai 3
            print("AI's choice: Paper")
            print("The AI Won!")
    # third case
    elif playerChoice == 3:
        print("Your choice: Paper")
        if aiChoice == 1: # ai 1
            print("AI's choice: Scissors")
            print("The AI Won!")
        elif aiChoice == 2: # ai 2
            print("AI's choice: Rock")
            print("You Won!")
        elif aiChoice == 3: # ai 3
            print("AI's choice: Paper")
            print("Tie!")
    else:
        print("Invalid Input.")

# calling main-func
main()