'''
Prints The Ein mal Eins

'''

from time import sleep

def main():
	min = 1
	max = 10
	for i in range(min, max+1):
		for j in range(min, max+1):
			print("{0} x {1} = {2}".format(i, j, i*j))
			sleep(0.1)
		print("")
		sleep(0.1)


main()