#python3

'''
This Program Calculates and Shows All the Sifferent Ways a Number Can Grow.

'''


# imports 
import math, time
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

# vars
num = 1


# funcs
def linearGrowth():
	# func represents linear growth

	# equation: y = m*x + n
	m = 2
	n = 0
	for x in range(100):
		y = (m*x) + n
		print("Iteration Number: {0} --> {1}".format(x, y))
		sleep(0.1)


def quadraticGrowth():
	# func represents quadratic growth

	for x in range(100):
		y = x**2
		print("Iteration Number: {0} --> {1}".format(x, y))
		sleep(0.1)


def expGrowth():
	# func represents exponential growth

	global num
	
	y = num = 1.05
	temp = num

	for i in range(100): # growing the number num
		num = num ** i# exponentially increasing num
		i += 1
		#print("Iteration number: {0} --> {1}".format(i, num))
		#sleep(0.1)
		num = temp


def logGrowth():
	base = 0.5
	for x in range(1, 10):
		y = math.log(x, base)
		print("Iteration Number: {0} --> {1}".format(x, y))
		sleep(0.1)	



# main func
def main():
	expGrowth()

# calling main-loop
main()

