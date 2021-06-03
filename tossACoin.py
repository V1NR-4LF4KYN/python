'''
Coin Tossing Program
    --> Can Flip a Coin however many times the User wants.
    --> Records Number of Tails and of Heads /--> Made it a TAD overcomplicated xD
    
    
'''

# Imports
import random, time;
import Clock

# Class
class Coin:
    '''  Coin Class '''
    def __init__(self):
        self.tail: int = 1; # Value of Tail
        self.head: int = 2; # Value of Head
        self.toss: int = 0; # Current Value after a Toss --> Either one or two (1 || 2)
        self.amount: int = 0; # Amount of times the coin gets flipped
        self.tails: List[int] = [] # List of Tails
        self.heads: List[int] = [] # List of Heads
        self.countTails: int = 0 # Number of Tails
        self.countHeads: int = 0 # Number of Heads
        
    
    # Funcs
    # Defining Getters
    def getTail(self):
        return self.tail;
    
    def getHead(self):
        return self.head;
    
    def getToss(self):
        return self.toss;
    
    def getAmount(self):
        return self.amount;
    
    # Counting Tails
    def getCountTails(self):
        for item in self.tails:
            self.countTails += 1;
        return self.countTails;
    # Counting Heads
    def getCountHeads(self):
        for item in self.heads:
            self.countHeads += 1;
        return self.countHeads;
    
    # Defining Setter
    def setAmount(self):
        self.amount = int(input('Enter how many times You want to flip the Coin: '));
    
    
    # Flipping the Coin
    def flip(self):
        self.setAmount();
        
        for _ in range(self.amount): # Adding either Tail or Head to According List
            self.toss = random.randint(self.tail, self.head);
            if self.toss == self.tail:
                self.tails.append(self.toss);
            else:
                self.heads.append(self.toss);
        
        if self.amount == 1: # Only one Coin-Toss
            if self.toss == self.tail:
                return 'You got Tail.';
            else:
                return 'You got Head.';
        else: # More than one Coin-Toss
            return f'Number of Tails: {self.getCountTails()} \nNumber of Heads:\
{self.getCountHeads()}';



# Main Function
def main():
    clock = Clock.Clock();
    startTime = time.time();
    c1 = Coin();
    print(c1.flip());
    clock.measureTime();

# Calling Main
main();