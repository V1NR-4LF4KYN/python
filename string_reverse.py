def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str

string = "python.science"
print("The original string is: ", string)
print("The reversed string is: ", reverse(string))