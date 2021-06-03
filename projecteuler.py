#in this program i will solve euler's problems
#python3


#imports
import time
import math


def one():
    
    solution = 1 # declaring solution
    for i in range(999): # all solutions below 1000
        if solution % 5 == 0 or solution % 3 == 0:
            print(solution)
        solution = solution + 1

#-----------------------------------------------

def two():
    n1, n2 = 1, 2 # first two terms
    limit = 4E6 # limit of sequence
    count = 0

    while count < 100:
        fibonacci = n1 + n2 # declaring fibonacci

        # condition of fibonacci being even and below the limit
        if fibonacci % 2 == 0 and fibonacci < limit:
            print(fibonacci)

        # update values
        n1 = n2
        n2 = fibonacci
        count += 1

#-----------------------------------------------

def three(n): # so far only gives all prime factors.....
    # A function to print all prime factors of  
    # a given number n 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print (2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3, int(math.sqrt(n))+1, 2): 
          
        # while i divides n, print i ad divide n 
        while n % i == 0: 
            print (i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print (n)



#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------

#change here for problem pid
def main():
    print("ENJOY\n\n") #greeting
    time.sleep(0.5)

    # problem to run
    three()
    

# calling main func
main() 
