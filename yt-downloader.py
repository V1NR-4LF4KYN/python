#python3

'''
This code will let you enter a Link to a YouTube Video.
Then it will proceed to Download given Video.

Author: XxVinr_AlfakynxX
Version: 1.0
'''

# install library
def libInstall():
    try:
        import os
        os.system("pip3 install youtube-python")
    except:
        print("Error during lib-install...")

#libInstall()

# imports
import yt

