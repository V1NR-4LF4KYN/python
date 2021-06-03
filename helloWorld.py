#python3

print("Hello World! \n") #simplest method

#using a variable
hello_world = "Hello World!"
print(hello_world)
print("")


#trying to fill a list and to print each character

list = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!", ""]

for i in list:
    print(i)


#now with the same list i wanna print "Hello World" in a single line

print("".join(list))

