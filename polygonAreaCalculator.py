'''
Polygon Area Calculator.

'''

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
    
    # funcs
    def setAttributes(self):
        self.a = float(input('Enter side length of the square: '))
    
    def calculateArea(self):
        self.area = self.a**2
        print(f'The square has the area {self.area}')
    
    def calculateScope(self):
        self.scope = self.a*4
        print(f'The square has the scope {self.scope}')



''' Third Project ---> Probability Calculator'''



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
    pass

# main-func
def main():
    secondProject()
    
# calling main
main()
