import random

count = 0

one=1
two=2
three=3
four=4
five=5
six=6
special=0

numbersGen = [one, two, three, four, five, six, special]

for i in range(6):
    numbersGen[i] = random.randint(1,49)

#uOne, uTwo, uThree, uFour, uFive, uSix, uSpecial



print(numbersGen)



uOne = int(input("Enter first number: "))
uTwo = int(input("Enter second number: "))
uThree = int(input("Enter third number: "))
uFour = int(input("Enter fourth number: "))
uFive = int(input("Enter fifth number: "))
uSix = int(input("Enter sixth number: "))

uSpecial = input("Enter super number: ")

numbersUser = [uOne, uTwo, uThree, uFour, uFive, uSix]



def compare_lists(x, y):
    global count
    equals = set(x).intersection(y)
    
    for equal in equals:
        count += 1
    
    return count
        

def getWin():
    if count == 0:
        print("You won nothing. Try again next time\n")
    elif count == 1:
        print("You got one number right. Maybe you have more luck next time!")
    elif count == 2:
        print("You got two numbers right. Not bad but I wish you more luck next time!")
    elif count == 3:
        print("You got three numbers! Really well done")
    elif count == 4:
        print("Wow, four correct guesses! Keep it up!")
    elif count == 5:
        print("Dang, almost got super lucky there!")
    elif count == 6:
        print("You must be a God or something")
    elif count == 7:
        print("Holy Crap! You cracked the JackPot!!!")
    
    
    

compare_lists(numbersGen, numbersUser)
getWin()
    
    
    
    
    
