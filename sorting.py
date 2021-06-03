# imports 
import random

# vars
list = []

# funcs

def fillList(list, n):

	for i in range(n+1):
		list.append(i)
	#print("The List: {0}\n".format(list))


def shuffle(list):
	# shuffling given list
	for _ in range(len(list)):
		# indexes at which to switch numbers in list
		switch = random.randint(0, len(list)-1)
		switch2 = random.randint(0, len(list)-1)
		if switch2 == switch:
			switch2 = random.randint(0, len(list)-1)

		# switching to numbers
		temp = list[switch]
		list[switch] = list[switch2]
		list[switch2] = temp

	print("The List after shuffling: {0}\n".format(list))	

def reverseList(list):
	# reversing a list
	print("The List after reversing: {0}\n".format(list))	


# sorting algorithms

def bubbleSort(list):
	counter = 1
	# sorting given list by comparing two elements each time. time = O(n²)
	for i in range(0, len(list)-counter):
		counter += 1
		for j in range(0, len(list)-1):
			if list[j] > list[j+1]:
				temp = list[j+1]
				list[j+1] = list[j]
				list[j] = temp

	print("The List after sorting via bubblesort: {0}\n".format(list))		


def selectionSort(list):
	# right now more like a bubblesort i think
	for j in range(len(list)):
		for i in range(len(list)-1):
			if list[i] > list[i+1]:
				lowestIndx = i+1
			else:
				lowestIndx = i

			temp = list[i]
			list[i] = list[lowestIndx]
			list[lowestIndx] = temp

	print("The List after sorting via selection sort: {0}\n".format(list))


# main-func
def main():
	global list
	fillList(list, 100)
	#reverseList(list)
	shuffle(list)
	# bubbleSort(list)
	selectionSort(list)

# calling main-func
main()
