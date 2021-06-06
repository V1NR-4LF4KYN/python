# Program will have to prime numbers
#
# What is a prime number? 
# It is a whole number greater than one. 
# Prime numbers are divisible only by the number 1 or itself.  
# E.g.: 2, 3, 5, 7 and 11 
#
#
# Figuring out the prime numbers:
# -------------------------------------------
# To prove whether a number is a prime number, 
# first try dividing it by 2, 
# and see if you get a whole number. 
# If you do, it can't be a prime number. 
# If you don't get a whole number, next try dividing 
# it by prime numbers: 3, 5, 7, 11 (9 is divisible by 3) and so on, 
# always dividing by a prime number
# -------------------------------------------
#
#



class Prime: 
	def __init__(self, limit: int):
		self.limit: int = limit 			# limits the max prime number generated
		self.numbersToLimit = []			# list of all whole numbers up to limit
		for i in range(self.limit):			# filling list with numbers using for loop
			self.numbersToLimit.append(i+1)
		self.prime_numbers = []				# list for all the prime numbers



	def getAllPrimeNumbers(self):
		for num in self.numbersToLimit:
			if((num != 1) and (not num % 2 == 0)): 	# see instructions at the top
				self.prime_numbers.append(num)

		return self.prime_numbers

t = Prime(12)
print(t.getAllPrimeNumbers())