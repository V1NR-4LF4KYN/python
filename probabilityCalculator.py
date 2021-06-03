'''
Probability Calculator

'''

# imports
import random

# classes
class Hat:
    def __init__(self):
        self.n = 0
        self.ballCount = 0
        self.register: List[int] = []
        self.average = 0
        self.counter = 0
        self.sum = 0
        
        
    # setters
    def setN(self):
        self.n = int(input('What is n? '))
    
    # getters
    def getN(self):
        return self.n
    
    
    # funcs
    def pickBalls(self):
   	 self.ballCount = random.randint(1, self.n + 1)
        print(f'Number of picked balls is {self.ballCount}. ')
        
    def main(self):
        self.setN()
        for _ in range(1000):
            self.pickBalls()
            self.register.append(self.ballCount)
        
        for item in self.register:
            self.counter +=1
            self.sum += item
        self.average = self.sum/self.counter
        print(f'Average pick with {self.n} is: {self.average}. ')
        
        

# main-func
def main():
    h = Hat()
    h.main()
    
# calling main
main()
