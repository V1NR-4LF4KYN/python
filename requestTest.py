'''
Testing The Request Module and it's Possibilities.

'''

# Imports
import requests
import threading

# Function
def main(): 
    x = requests.get('https://w3schools.com/python/demopage.htm');
    if x:
        print('Success');
    else:
        print('Error');

# Calling Main Function + making a thread out of it.
t = threading.Thread(target=main)
t.start()
t.join()