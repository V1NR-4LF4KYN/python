#python3

'''
Testing a generator in Python3
And of course comparing it with a standard method of iterating

'''


def customRange(count): # replacing the built-in range() with a custom generator
    num = 0
    while num < count:
        yield num
        num += 1

def cRange(count):
    num = 0
    for i in count:
        yield num
        num += 1


for i in customRange(20):
    print(i)
    
for i in cRange(20):
    print(i)