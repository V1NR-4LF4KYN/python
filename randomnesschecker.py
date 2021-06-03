#!usr/bin/python3.8

# imports
import random as r

# vars
a = 0
b = 0
percentage = 0
sum = 0
l = []

# funcs
def checkRandomness(n):
	global a, b

	# get a statistic
	for i in range(n):
		rand = r.randint(0,1)
		if rand == 0:
			a += 1
		elif rand == 1: 
			b += 1
		else:
			print("Error")
			break

	# calculate the percentage
	percentage = (a/b) * 100
	l.append(percentage)
	#print(percentage)



def iterate(n):
	global a, b, sum, percentage
	for i in range(n):
		checkRandomness(1000)
		
	for item in l:
		sum += item

	sum = sum/len(l)
	#print(sum)


def getStatistic(n, per):
	withinPer = 0
	whoutPer = 0

	
	for i in range(n):
		iterate(100)

		if sum <= (100+per) and sum >= (100-per):
			withinPer += 1
		elif sum > (100+per) or sum < (100-per): 
			whoutPer += 1
		else:
			print("ERROR")
			break
	print(withinPer, whoutPer)
	if withinPer == 0 or whoutPer == 0:
		per = 0
	else:
		per = (withinPer/whoutPer) * 100
		#per = int(per)
	
	print(per)


def main():
	getStatistic(50, 1)
	

main()