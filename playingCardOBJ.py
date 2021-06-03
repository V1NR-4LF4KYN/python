#python3

'''
Quick Explanation of a Card Deck:
--------------------------------------------------------------
 - A deck consists of 52 cards
 - There are 13 of each suit Clubs, Diamonds, Hearts, and Spades inside a deck

'''

# imports
import random
import numpy as np

# vars
persons = ["Club", "Diamond", "Heart", "Spade"]
numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

# class
class Card(object):
    def __init__(self, number, person):
        self.number = number
        self.person = person



# getting a random Card
def getRandCard(count):
    for i in range(count):
        randCard = Card(persons[random.randint(0, len(persons)-1)],
                        numbers[random.randint(0, len(numbers)-1)])
        
        print(randCard.person, randCard.number)

# getting 10 random Cards
getRandCard(10)