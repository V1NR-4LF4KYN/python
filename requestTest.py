'''
Testing The Request Module and it's Possibilities.

'''


# Imports
import requests

# Function
def main(): 
    x = requests.get('https://w3schools.com/python/demopage.htm');
    if x:
        print('Success');
    else:
        print('Error');

# Calling Main Function
main();