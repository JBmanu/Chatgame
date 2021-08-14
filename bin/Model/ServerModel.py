"""
@author: buizo
"""
import socket
import threading

class ServerModel():
    HOST_ADDR = '127.0.0.1'
    HOST_PORT = 8080
    
    SERVER_LISTENING = 5;

    def __init__(self):
        self.server = None;
        self.client_name = " "
        self.clients = []
        self.clients_names = []
        self.player_data = []


    def initServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        print(socket.AF_INET)
        print(socket.SOCK_STREAM)

        self.server.bind((self.HOST_ADDR, self.HOST_PORT));
        self.server.listen(self.SERVER_LISTENING);
        
        


