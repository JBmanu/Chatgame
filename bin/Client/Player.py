
from ClientModel import ClientModel as Model
from ChatGUI import ChatApplication as ChatGUI
from LoginGUI import LoginApplication as LoginGUI
from threading import Thread
import tkinter as tk


chatGUI = ChatGUI();
loginGUI = LoginGUI();
client = Model();

loginGUI.pulsante_login.config(command = lambda: startConnection());

def startConnection():
    if(checkLogin()):
        client.connect();
        loginGUI.destroy();
        chatGUI.deiconify();
    else:
        loginGUI.cleanEntryLogin();
        loginGUI.login_head_label.config(text = "Dati sbagliati, scemo")

    RECEIVE_THREAD = Thread(target = receive)
    RECEIVE_THREAD.start()
    

def receive():
    while True:
        try:
            #quando viene chiamata la funzione receive, si mette in ascolto dei messaggi che
            #arrivano sul socket
            msg = client.socket.recv(Model.BUFSIZ).decode("utf8")
            #visualizziamo l'elenco dei messaggi sullo schermo
            #e facciamo in modo che il cursore sia visibile al termine degli stessi
            chatGUI.text_widget.insert(tk.END, msg)
            # Nel caso di errore e' probabile che il client abbia abbandonato la chat.
        except OSError:  
            break


def checkLogin():
    if (loginGUI.host_entry.get() == Model.HOST):
        client.serverHost = loginGUI.host_entry.get()

    if (loginGUI.port_entry.get() == str(Model.PORT)):
        client.serverPort = loginGUI.port_entry.get()

    if(client.serverHost != " " and client.serverPort != " "):
        client.nickname = loginGUI.nick_entry.get()
        return True

    return False


chatGUI.mainloop();
loginGUI.mainloop();