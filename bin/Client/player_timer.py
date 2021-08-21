
from threading import Timer
from time import sleep
from time import os, threading


class PlayerTimer():
    

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
    


















   