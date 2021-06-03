#python3

'''
Script that moves images from my Downloads Folder to the Pictures folder.

'''

# imports
import os

# funcs
def movePix():
    os.system("cd; ")
    os.system("mv Downloads/*.jpeg Pictures/")
    os.system("mv Downloads/*.jpg Pictures/")
    os.system("mv Downloads/*.png Pictures/")
    os.system("mv Downloads/*.svg Pictures/")


def main():
    movePix()

if __name__ == "__main__":
    main()