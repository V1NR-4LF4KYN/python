# imports
from random import randint as r

# funcs
def computerguess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        guess = r(low, high)
        feedback = input(f'Is {guess} lower (L), higher (H) or the correct (C) guess? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yaaaay, {guess} was correct!')
    
    
# main-func
def main():
    computerguess(500)

# calling main
main()