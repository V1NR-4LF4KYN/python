#python3 

'''
A Simple C-Matrix Clone.

Author: XxVinr_AlfakynxX
Version: 1.0
'''

# imports
import random

# vars
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# funcs
def main():
    for _ in range(12):
        print(random.choice(chars))


# calling main-loop
main()