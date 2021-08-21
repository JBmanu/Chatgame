
from time import sleep
import threading as Thread

class Timer():
    
    TIMER = 30;
    END_TIME = 0;

    MSG = "Ho finito il tempo"

    def __init__(self):
        self.time = self.TIMER;


    def startTimer(self):
        self.thread = Thread(target = self.countdown()).start()


    def countdown(self):
        try:
            while self.time > self.END_TIME:
                print(self.time)
                self.time -= 1;
                sleep(1);
        except TypeError:
            print("hai finito il tempo")
            

    def endTIme(self):
        return self.END_TIME;

    


















   