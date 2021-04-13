import makeNumReadable as m


# vars
n_int = 1
n_str = str(n_int)
maxLenNum = 36


# help func
def addZeroToN():
    global n_int, n_str
    n_str += '0'
    n_int = int(n_str)


# increasing the number to be printed 
for i in range(maxLenNum):
    print(m.makeNumReadable(n_int))
    addZeroToN()
