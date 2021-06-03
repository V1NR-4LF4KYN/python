#python3
#writing

import sys, time

# letting text be written in front of your eyes
def sp(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

# sets space between each line        
def space():
    print("")
    print("")
    

sp("Hello World")
print("Print: Hello World")
