'''
A little Budget App.

'''

# classes
class Budget:
    # total budget
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.categories = []
    
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
    
    
# functions
def budgetFunc():
    b = Budget()
    b.setIncome()
    b.setExpenseList()
    b.setExpenses()
    b.subtractExpenses()
    print(b.getIncome())

# main-func
def main():
    budgetFunc()
    
# calling main
main()
