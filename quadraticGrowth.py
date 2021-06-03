#python3

'''
This Program Represents Quadratic Growth.

'''

# imports
from time import sleep


# funcs
def main():
	# equation: y=x**2

	for x in range(100):
		y = x**2
		print("Iteration Number: {0} --> {1}".format(x, y))
		sleep(0.0)


# calling main-loop
main()
