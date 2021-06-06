'''
Three Challenges I found on the net for practicing Classes in Python3.
Source: https://towardsdatascience.com/3-useful-projects-to-learn-python-classes-cf0076c36297

Help I used to learn classes:
 - https://www.w3schools.com/python/python_classes.asp
 - https://www.tutorialspoint.com/python/python_classes_objects.htm
 - https://codereview.stackexchange.com/questions/173486/simple-budget-program

'''

# imports
import random

# classes

''' First Project ---> Budget App '''

class Budget:
    # total budget
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.categories: List[str] = []
    
    # getters
    def getIncome(self):
        if self.income >= 0:
            return f'\nYou are in positive. \nIn total you have {self.income}€ left over.'
        else:
            return f'\nYou are in negative. \nIn total you have {self.income}€ left over.'
    
    # setters
    def setIncome(self):
        self.income = float(input('Please enter the amount of income you get: '))
        print(f'You get {self.income}€')
    
    def setExpenses(self):
        for item in self.categories:
            self.expenses += float(input(f'How much do you spend on {item}? '))
    
    #funcs
    
    def setExpenseList(self):
        addingExpenses = True
        while addingExpenses:
            inp = str(input('Do you want to add an expense? Y or N? ')).lower()
            if inp == 'y':
                self.categories.append(str(input('Enter what expense you would like to add: ')))
            elif inp == 'n':
                addingExpenses = False
            else:
                print('An error occurred! Enter Y or N only...')
    
    
    def subtractExpenses(self):
        if self.categories: #if categories has a expense in it
            self.income -= self.expenses
        else:
            print('There are no expenses.')
    
    
    
    

''' Second Project ---> Polygon Area Calculator '''

class Rectangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = self.a
        self.d = self.b
        self.area = 0
        self.scope = 0
    
    #funcs
    def setCalculation(self):
        inp = input('What shape do you want to work with? Rectangle (R), Square (S): ').lower()
        if inp == 'r':
            shape = Rectangle()
        elif inp == 's':
            shape = Square()
        else:
            pass
        shape.setAttributes()
        shape.calculateScope()
        shape.calculateArea()
        shape.getA()
        
    def setAttributes(self):
        self.a = float(input('Enter a value for a: '))
        self.b = float(input('Enter a value for b: '))
        
    def calculateArea(self):
        self.area = self.a * self.b
        print(f'The rectangle has the area {self.area}')
    
    def calculateScope(self):
        self.scope = self.a * 2 + self.b * 2
        print(f'The rectangle has the scope {self.scope}')
        
    # getter
    def getA(self):
        print(f'Side a has a value of: {self.a}. ')
        
class Square(Rectangle):
    def __init__(self):
        super().__init__()
    
    #funcs
    def setAttributes(self):
        self.a = float(input('Enter side length of the square: '))
    
    def calculateArea(self):
        self.area = self.a**2
        print(f'The square has the area {self.area}')
    
    def calculateScope(self):
        self.scope = self.a*4
        print(f'The square has the scope {self.scope}')



''' Third Project ---> Probability Calculator'''

class Hat:
    def __init__(self):
        self.n = 0
        self.ballCount = 0
        self.register: List[int] = []
    
    # setters
    def setN(self):
        self.n = int(input('What is n? '))
    
    # getters
    def getN(self):
        return self.n
    
    
    # funcs
    def pickBalls(self):
        self.ballCount = random.randint(1, self.n)
        print(f'Number of picked balls is {self.ballCount}. ')
        
    def main(self):
        self.setN()
        for i in range(1000):
            self.pickBalls()
            self.register.append(self.ballCount)
        
        self.average = 0
        self.counter = 0
        self.sum = 0
        for item in self.register:
            self.counter +=1
            self.sum += item
        self.average = self.sum/self.counter
        print(f'Average pick with {self.n} is: {self.average}. ')
    
    
''' --------------- END OF PROJECT CLASSES CODE --------------- '''




# functions
def firstProject():
    b = Budget()
    b.setIncome()
    b.setExpenseList()
    b.setExpenses()
    b.subtractExpenses()
    print(b.getIncome())



def secondProject():
    r = Rectangle()
    r.setCalculation()


def thirdProject():
    h = Hat()
    h.main()

# main-func
def main():
    secondProject()
    
# calling main
main()