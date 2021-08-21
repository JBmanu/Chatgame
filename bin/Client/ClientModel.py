from socket import AF_INET, socket, SOCK_STREAM

class ClientModel():
    HOST = '127.0.0.1'
    PORT = 8080    

    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    
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
            print("ERROR!!! Cannot connect to host: " + self.HOST + " on port: " + str(self.PORT) + " Server may be Unavailable. Try again later")


    def checkLogic(self, host, port, nick):

        if (host == self.HOST and port == str(self.PORT)):
            self.serverHost = host
            self.serverPort = port
            self.nickname = nick
            return True

        return False



