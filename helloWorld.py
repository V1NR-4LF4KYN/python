#/usr/bin/python3

# vars
s = "Hello World"
arr = []

def helloWorld():
    global s, arr
    s = s
    for letter in s:
        arr.append(s)
    output = ''
    for item in arr:
        output += item
        output += " "

    
    return output
	
def main():
	print(helloWorld())

main()
