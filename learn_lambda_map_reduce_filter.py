# Learning the lambda function as well as the acompaniing reduce, map, and filter funcs.
#
# Using this tutorial: https://www.python-course.eu/python3_lambda.php
#
# Author: James Roper
# 02.06.2021 



sum = lambda x,y: x + y 		# A Basic Lambda Function

def sum(x, y): 					# And the equivalent as a normal function
	return x + y

print(sum(5,4)) 				# Testing these funcs.



# The Map function makes it better and more practical.
# Map func takes to params

# r = map(func, seq)  

# The first argument func is the name of 
# a function and the second a sequence (e.g. a list) seq. 
# map() applies the function func to all the elements of the sequence seq.



def fahrenheit(T):
    return (round((float(9)/5)*T + 32))

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)

print(f'Temperatures in celsius: {temperatures} \
	and rounded temperatures in fahrenheit: {list(F)}')