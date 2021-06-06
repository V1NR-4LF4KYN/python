'''
The Hangman Drawings.... imported in hangman.py

'''

# imports

# vars
bottomRowLength = 10
stickLength = 5
topRowLength = 8


# funcs
def firstStage():
	for i in range(bottomRowLength):
		print("_", end="")

def secondStage():
	for i in range(stickLength):
		print("   |")
	firstStage()

def thirdStage():
	for i in range(3):
		print(" ", end="")
	for i in range(topRowLength):
		print("-", end="")
	secondStage()

#def fourthStage():
#	for i in range():
#		pass



def main():
	pass

main()