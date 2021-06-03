#python3


# prints spaces in the output
def space():
    for count in range(2):
        print("")


# a class, aka a object in code
class Person:
    def __init__(self, name, age, height, slogan): # initiation func
        self.name = name
        self.age = age
        self.height = height
        self.slogan = slogan
        
    def main(self):
        print(f'{self.name} {self.age}')

user = Person("James", 18, 174, "No Risk, No Fun!")


import random
import time

starttime = time.time()

class R:
    def __init__(self, range):
        self.range = range
        self.value = random.randint(1,self.range)
    
    
    def getVal(self):
        return self.value;
    
    def setValue(self):
        self.value = random.randint(1, self.range)
    
    def setRange(self):
        self.range = int(input('Enter a range: '))
    

n = 1000000; #range for objects
m = 1000; #number of tries
counter = 0;
lst = [];
vals = []
sum = 0

def exp():
    global sum, counter, lst, n, m, vals
    for i in range(m):
            r = R(n);
            lst.append(r)
            counter += 1;
            
    for item in lst:
        sum += item.getVal()

    av = sum/counter
    lst = []
    vals = []
    sum = 0
    counter = 0
    print(f'I=[1; {n}]; Average in m={m} tries is: {av}') #for logging
    return av


def exp2():    
    lst2 = []
    counter2 = 0  
    sum2 = 0
    for i in range(1000):
        lst2.append(exp())
        counter2 += 1
        print(f'Iteration {counter2}; time: {time.time()-starttime} seconds ') #for logging
    
    
    for item in lst2:
        sum2 += item

    av2 = sum2/counter2
    print(f'The average is {av2}. So basically about half of {n} which equals {n/2}')
    



exp2()

takenTime = time.time() - starttime
if takenTime >= 60:
    takenTime /= 60
    if int(takenTime) > 1:
        print(f'Program took {int(takenTime)} minutes and {round((takenTime - int(takenTime))*60)} seconds to run.')
    else:
        print(f'Program took {int(takenTime)} minute and {round((takenTime - int(takenTime))*60)} seconds to run.')
else:
    print(f'Program took about {round(takenTime)} seconds to run.')