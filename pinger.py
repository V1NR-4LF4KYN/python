#python3

'''
This is a simple Ip-Pinger
The purpose of a pinger is to be an online/offline checker
Or it could be upgrade to be a DOS or even DDOS-Tool

'''

# imports
import os, time

# vars
hostname = "google.com"
response = ""


# funcs

#visuals
def ascii_greet():
    print("TODO: ASCII ART WELCOME")

def madeBy():
    print("Made By XxVinr_AlfakynxX (aka @vinralfakyn on IG)")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

#pinger itself
def getHostname():
    global hostname
    hostname = str(input("--=IP: "))

def grabbingSoulInfo():
    os.system("clear")
    print("TODO ASCII ART")
    time.sleep(1)
    print("getting the scythe...")
    time.sleep(0.5)
    os.system("clear")
    

def ping():
    isPinging = True
    counter = 0
    while isPinging:
        response = os.system("ping -c 4 -i 0.2 -n > /dev/null " + hostname)
        if response.returncode == 0:
            print("Reply from ", hostname, counter)
            counter += 1
            #time.sleep(0.3)
        else:
            isPinging = False
            for i in range(10):
                print("[*] OFFLINE [*] the reaper brought the scythe to reap ", hostname, "'s router")
                time.sleep(0.3)
            
        
        
# main-loop
def main():
    ascii_greet()
    madeBy()
    getHostname()
    grabbingSoulInfo()
    ping()

# calling main func
main()
print("")