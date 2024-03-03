#!/usr/bin/env python3
import sys
import time

def maintask():
    """ lets start basic so we can import into the compose file
    """
    print(" hello world \n")
    for x in range(0, 10, 1):
        print(f" hello world {x}\n", flush=True)
        
        time.sleep(1)



if __name__ == "__main__":
    sys.exit(maintask())
