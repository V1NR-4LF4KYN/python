'''
Class: Clock! 

    --> Can Measure Time since an Instance of Clock was created!
    --> Can make your program wait!

'''

# Imports
import time;

# Class
class Clock:
    def __init__(self):
        self.startingTime = time.time(); # Initiates 
        self.takenTime = 0
    
    # Setters
    def setStartingTime(self):
        self.startingTime = time.time();
    
    # Functions
    def wait(self, seconds): # Programm Waits
        time.sleep(seconds);
    
    def measureTime(self): # Measures Time between call The Function and Creation of Clock Object
        self.takenTime =  time.time() - self.startingTime;
        print(f'Time: {self.takenTime}s.');
        return self.takenTime;
