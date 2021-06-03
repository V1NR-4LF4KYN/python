#python3

# imports
import os

def shutdown():
    os.system("shutdown -h now")

# main-loop
def main():
    shutdown()

# calling main func
main()