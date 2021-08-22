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
        self.sockets = {}
        self.address = {}


    """ Apre la socket, la connessione con il client e si mette in scolto """
    def openSocket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        print(socket.AF_INET)
        print(socket.SOCK_STREAM)

        self.server.bind(self.IP);
        self.server.listen(ServerClient.SERVER_LISTENING);


    """ La funzione invia un messaggio in broadcast a tutti i client."""
    def closeAllConnections(self):
        for k in self.clients.keys():
            k.close();


    """ La funzione invia un messaggio in broadcast a tutti i client."""
    def sendBroadcast(self, msg, prefisso=""):
        for client in self.sockets:
            client.send(bytes(prefisso, "utf8") + msg)


    """ La funzione invia un messaggio in broadcast a tutti i client, tranne a uno specifico"""    
    def sendBroadcastWithout(self, client, msg, prefisso=""):
        for utente in self.sockets:
            if (utente != client):
                utente.send(bytes(prefisso, "utf8") + msg)


    """ La funzione chiude la connessione di uno specifico client """
    def quitClient(self, client):
        self.sendBroadcast(bytes("%s ci lascia, ha quittato \n" % self.sockets[client], "utf8"))
        del self.sockets[client]
        client.close()


    """ La funzione manda un messaggio in stringa ad uno specifico client """
    def sendStringMsgToClient(self, client, msg):
        client.send(bytes(msg + "\n", "utf8"))

    
    """ La funzione manda un messaggio in bytes ad uno specifico client """
    def sendBytesMsgToClient(self, client, msg):
        client.send(msg)

    
    """ La funzione manda un messaggio che un client si e unito al gioco agli altri giocatori"""
    def sendEnterGameMsg(self, client, name):
        msg = "%s si è unito al gioco! \n"  % name
        self.sendBroadcastWithout(client, bytes(msg, "utf8"))