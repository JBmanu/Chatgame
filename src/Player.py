
from ClientModel import ClientModel as Model
from ChatGUI import ChatApplication as ChatGUI
from LoginGUI import LoginApplication as LoginGUI
from UtilitiesSC import UtilitiesSC as ServerClient

from threading import Thread

chatGUI = ChatGUI();
loginGUI = LoginGUI();
client = Model();

loginGUI.pulsante_login.config(command = lambda: startConnection());

chatGUI.pulsante_invio.config(command = lambda : send())

chatGUI.pulsante_a.config(command = lambda : sendDefaultChar("a"))
chatGUI.pulsante_b.config(command = lambda : sendDefaultChar("b"))
chatGUI.pulsante_c.config(command = lambda : sendDefaultChar("c"))
chatGUI.pulsante_quit.config(command = lambda : quitGame())


# Instaura la connessione con il server
def startConnection():
    if(client.checkLogic(
        loginGUI.host_entry.get(),
        loginGUI.port_entry.get(), 
        loginGUI.nick_entry.get())):

        client.connect();
        client.socket.send(bytes(client.nickname, "utf8"));

        loginGUI.destroy();
        chatGUI.deiconify();

        Thread(target = receive).start()
    else:
        loginGUI.cleanEntryLogin();
        loginGUI.login_head_label.config(text = "Dati sbagliati, scemo")


# Funzione per l'invio predefinito per la scelta della domanda
def sendDefaultChar(char):
    chatGUI._inserisci_messaggio(char, "Tu")
    client.socket.send(bytes(char, "utf8"))


# Funzione per l'invio del messaggio al server tramite il bottone invio o tasto invio
def send(event=None):
    msg = chatGUI.msg_entry.get();

    if(msg == "quit"):
        quitGame();
    else:
        chatGUI._inserisci_messaggio(msg, '\n\n' + "Tu");
        client.socket.send(bytes(msg, "utf8"))

chatGUI.msg_entry.bind("<Return>", send)


# Funzione per la ricezione dei messaggi dal server al client
def receive():
    while True:
        try:
            #quando viene chiamata la funzione receive, si mette in ascolto dei messaggi che arrivano sul socket
            msg = client.socket.recv(ServerClient.BUFSIZ).decode("utf8")
            chatGUI.insertMsgFromTextToChat(msg)
        except OSError:  
            break


# per uscire dalla partita
def quitGame():
    client.socket.close();
    chatGUI.destroy();


chatGUI.mainloop();
loginGUI.mainloop();