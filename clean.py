#!/usr/bin/python3
''' Function For Cleaning Files of Unnecessary Spaces at the End of Lines '''

def cleanCode(file):
    with open(file, "r") as f: # open file to read
        fileText = "" # string with cleaned content of data
        for line in f:
            fileText += " ".join(line.split())+"\n"
    with open(file, "w") as t: # overwrite file with cleaned data
        t.write(fileText)
