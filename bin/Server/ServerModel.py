"""
@author: buizo
"""
import socket

class ServerModel():
    HOST_ADDR = '127.0.0.1';
    HOST_PORT = 8080;
    BUFSIZ = 1024;
    IP = (HOST_ADDR, HOST_PORT);

    SERVER_LISTENING = 5;
    
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
        self.server.listen(self.SERVER_LISTENING);

