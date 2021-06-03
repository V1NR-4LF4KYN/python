#python3

# imports
import os

def mkdir():
    os.system("mkdir /media/pi/tdk/python_backup")

def backup():
    mkdir()
    
    os.system("cp /home/pi/python/* /media/pi/tdk/python_backup")


def main():
    try:
        backup()
        print("Finished")
    except:
        print("ERROR Occured")
    finally:
        os.system("echo exiting...")
        print("Exiting...")


