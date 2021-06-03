'''
OOP Version of Game - FizzBuzz

The Players count. When they get to 3 - any multiple of 3 - they have to say "FIZZ"
And any mutliple of 5 they say "BUZZ"
If their number is a multiple of 3 And 5 the have to say "FIZZBUZZ"

'''
# imports
from time import sleep as s
# classes
class FizzBuzz:
    def __init__(self):
        self.range = 0
    
    def setRange(self):
        self.range = int(input('What should be the range to which is counted? '))
    
    def play(self):
        for i in range(1, self.range+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FIZZBUZZ")
            elif i % 3 == 0:
                print("FIZZ")
            elif i % 5 == 0:
                print("BUZZ")
            else:
                print(i)
            s(0.01)
    
    def main(self):
        self.setRange()
        self.play()
    
# main-loop
def main():
    g1 = FizzBuzz()
    g1.main()

# calling main func
main()
