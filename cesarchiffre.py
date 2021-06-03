'''
This program will take a string and and an integer.
The String will be encrypted with the Cesar-Cipher.
The characters of the String will be replaced by other chars
that are in the place in the alphabet the given integer suggests.

'''

# vars
sentence = ""
cipherInt = 0

# funcs
def getSentence():
    global sentence
    print('Enter a sentence to be encrypted: \n')
    sentence = input(": ")
    sentence = sentence.lower()
    
def getCipherInt():
    global cipherInt
    print('Enter a number encrypt with: \n')
    cipherInt = input(": ")
    
def encrypt():
    print("Before: ")
    print(sentence)
    print(cipherInt)
    for char in sentence:
        char += cipherInt
        print(char)
    print("After: ")
    print(sentence)


# main-loop
def main():
    getSentence()
    getCipherInt()
    encrypt()

# calling main func
main()