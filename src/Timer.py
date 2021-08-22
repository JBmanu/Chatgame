
from time import sleep
import threading as Thread

class Timer():
    
    TIMER = 20;
    END_TIME = -1;

    MSG = "Ho finito il tempo"

    def __init__(self):
        self.time = self.TIMER;

    def decrTime(self):
        self.time -= 1;
        

    


















   