"""
@author: buizo
"""

from socket import AF_INET, socket, SOCK_STREAM
from ServerModel import ServerModel as Server

class ClientModel():

    def __init__(self):
        self.socket = None;

        self.nickname = " ";
        self.serverHost = " ";
        self.serverPort = " ";

    def connect(self):
        try:
            self.socket = socket(AF_INET, SOCK_STREAM)
            self.socket.connect((self.serverHost, int(self.serverPort)))
        
        except Exception as e:
            print("ERROR!!! Cannot connect to host: " + Server.ADDR + " on port: " + str(Server.PORT) + " Server may be Unavailable. Try again later")


    def checkLogic(self, host, port, nick):

        if (host == Server.ADDR and port == str(Server.PORT)):
            self.serverHost = host
            self.serverPort = port
            self.nickname = nick
            return True

        return False



