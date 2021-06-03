#!/usr/bin/python3.8

'''
A Simple Hangman Game

'''

# imports
from random import randint as rand
from time import sleep as s

# vars
running = True

words = ["Hallo", "Welt", "Auto", "Halloween", "Kürbis", "Hund", "Katze", "Besenkammer", "Hausmeister", "Schule", "Polizei", "Fahrschule", "Qualle", "Affe", "Haus", "Baum", "Garten", "Apfelschorle", "Wasser", "Katie", "James", "Welle", "Connor", "Apfelsaft", "Mutti", "Daddy", "Ruby", "Toffee", "Maske", "Regen"]

word  = str("")
letters = []

guessed = []
endWord = ""

errorCount = 0

# funcs
def getWord(wordlist):
    # choose a word from given list and add to letters
    global letters, word
    word = wordlist[rand(0, len(wordlist)-1)]

    for letter in word: # add each letter of word to letters
        letters.append(letter.lower())



def guessLetters():
    global letters, word, guessed, running, endWord, errorCount
    
    while running:
        # print the dashes so you can see what you got right already
        for item in letters:
            if item not in guessed: # print a dash if the letter is not already guessed
                print("_", end=" ")
            elif item in guessed: # if the letter has been guessed print the letter
                print(item, end=" ")
            else:
                print("ERROR")
                break

        print("")

        # let the user guess
        guess = input("\nGuess a letter: ").lower()
        guess = guess[0] # ensures only the first given letter is used or compared
        # append guessed letter to guessed letters and remove from list of letters to guess
        if guess in letters and guess not in guessed:
            # for-loop so that letters that occur more than once also get added
            for correctGuess in letters:
                if correctGuess == guess: # check if the letter is the guessed one -> if so add it 
                    guessed.append(correctGuess)
                    endWord += correctGuess
        else: 
            errorCount += 1
        print("Your Error Count: {0}".format(errorCount))
        print("")


        # end game if all the letters where guessed or max error count is reached
        if len(endWord) ==  len(word):
            print("Du hast gewonnen! Gut gemacht!")
            running = False
        elif errorCount >= 12:
            print("You Lost! Better Luck next time...")
            running = False





# main loop
def main():
    getWord(words)
    guessLetters()


# calling main func
main()