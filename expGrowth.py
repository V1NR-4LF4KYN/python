# imports
import time

# vars
num = 1.05


# funcs
def main():
	global num
	temp = num

	for i in range(100): # growing the number num
		num = num ** i# exponentially increasing num
		i += 1
		print("Iteration number: {0} --> {1}".format(i, num))
		time.sleep(0.1)
		num = temp




# calling main-loop
main()
