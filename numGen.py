# Generates a random number

import random

class Gen: 
	def __init__(self, lower, upper):
		self.lowerLimit = lower
		self.upperLimit = upper

	def generateNumber(self):
		return random.randint(self.lowerLimit, self.upperLimit)
