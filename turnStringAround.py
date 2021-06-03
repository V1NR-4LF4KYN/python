#python3

'''
In this little program a string is converted into a list char by char,
Then it gets reversed using List Comprehensions,
And then it gets converted into a String again

'''

# vars

string = "Hello, World!"
reversed_string = ""


# super short version, that also works
print(string)
print(string[::-1])



# long version
'''
print("This is the normal string: ")
print(string)
print("")

print("Now the string is a list")
string = list(string)
print(string)
print("")

print("And now we can join it to an empty string",
      "and reverse it at the same time:")
reversed_string = reversed_string.join(string[::-1])
print(reversed_string)
print(reversed_string[::-1])

'''

