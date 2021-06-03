# a calculator written in python
# idea is to write it simply as a terminal-prgram
# then i will use tkinter to add a gui
#
# author: James Roper
# -----------------------------------------


# imports
import math
import tkinter as tk


# code for calculator

# vars
pi = math.pi


# funcs
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2



# acutal responsive program
def run():
    # intro 
    print("Hello, welcome to my calculator\n")
    print("What kind of calculation do you want to make?")

    # asking for userinput
    userInput = input("Enter 'add', 'sub', 'multi' or 'div': \n")

    # deciding on what kind of equation to make
    # addition
    if userInput == "add": 
        n1 = int(input("Whats your first number?\n"))
        n2 = int(input("Whats your second number?\n"))
        print("The equation equals: ")
        print(addition(n1, n2))
    # subtraction
    elif userInput == "sub": 
        n1 = int(input("Whats your first number?\n"))
        n2 = int(input("Whats your second number?\n"))
        print("The equation equals: ")
        print(subtraction(n1, n2))
    # multiplication
    elif userInput == "multi": 
        n1 = int(input("Whats your first number?\n"))
        n2 = int(input("Whats your second number?\n"))
        print("The equation equals: ")
        print(multiplication(n1, n2))
    # division
    elif userInput == "div": 
        n1 = int(input("Whats your first number?\n"))
        n2 = int(input("Whats your second number?\n"))
        print("The equation equals: ")
        print(division(n1, n2))
    # exiting on non-acceptable user-input
    else: 
        print("\nERROR. Exiting...\n")



# my try on a gui

# variables for the gui
WIDTH = 700
HEIGHT = 800

def gui():
    
    root = tk.Tk() # main window
    root.title("My Calculator")
    
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) #basically sets the size of root
    canvas.pack()
    
    frame = tk.Frame(root, bg="#3377ff") #container for content
    frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
    
    entry = tk.Entry(frame, font="24")
    entry.grid(column="1", row="1")
    
    button_1 = tk.Button(frame, text="1")
    button_1.grid(column="1", row="2")
    
    
    '''    
    button = tk.Button(frame, text="My button") # a button
    button.pack()
    
    label = tk.Label(frame, text="This is a label", bg="yellow")
    label.pack()
    
    entry = tk.Entry(frame, bg="green")
    entry.pack()
    '''
    
    root.mainloop() # running the gui
    

# main func which is run in the end
def main(): 
    #tkinter._test()
    #run()
    gui()


# running of code
main()
