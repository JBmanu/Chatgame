import threading
from Player import Player
from MasterServer import MasterServer

player = Player();
master = MasterServer();

threading.Thread(target = Player().run()).start();
threading.Thread(target = MasterServer().run()).start();




