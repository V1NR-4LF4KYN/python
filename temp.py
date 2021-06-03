#!/usr/bin/python3
''' Function For Cleaning Files of Unnecessary Spaces at the End of Lines '''

def cleanCode(file):
with open(file, "r") as f: # open file to clean up
with open("temp.py", "a") as t:
for line in f:
t.write(" ".join(line.split())+"\n")




def cleantemp():
with open("temp.py", "w") as n:
n.write("")

def main():
cleantemp()
cleanCode("clean.py")

main()
