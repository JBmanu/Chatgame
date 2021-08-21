
from threading import Timer
from time import os, random, thread

class PlayerTimer():
    
    from time import *

import os
import random
import threading

guess=""
Gamewinner=0
n = random.randint(1, 99)
lives = 8
answer = "yes"

print("You have a total of 8 lives. A wrong guess would result in one less life.")
SingleOrDouble=input("Do you want single player or double player?")

def countdown():
    global my_timer
    
    my_timer=5

    for x in range(5):
        my_timer=my_timer-1
        sleep(1)
    print("Out of time")
    os._exit(1)

countdown_thread=threading.Thread(target=countdown)
countdown_thread.start()
    


















   