"""
@author: buizo
"""
from UtilitiesSC import UtilitiesSC as ServerClient
import socket

class ServerModel():
    ADDR = '127.0.0.1';
    PORT = 8080;
    IP = (ADDR, PORT);

    HEADER = "Master: ";

    def __init__(self):
        self.server = None;
        self.clients = {}
        self.address = {}


    def openSocket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        print(socket.AF_INET)
        print(socket.SOCK_STREAM)

        self.server.bind(self.IP);
        self.server.listen(ServerClient.SERVER_LISTENING);

