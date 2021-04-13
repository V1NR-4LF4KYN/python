import os;
import time;

try:
    while 1:
        os.system("df -h");
        time.sleep(1);
        os.system("clear");
except:
    print("\nDone");
