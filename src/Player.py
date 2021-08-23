
from ClientModel import ClientModel as Model
from ChatGUI import ChatApplication as ChatGUI
from LoginGUI import LoginApplication as LoginGUI
from UtilitiesSC import UtilitiesSC as ServerClient
from GameModel import GameModel as Game

from Timer import Timer 
from threading import Thread
from time import sleep

chatGUI = ChatGUI();
loginGUI = LoginGUI();
timer = Timer();
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

        Thread(target = printTImer).start()
        Thread(target = receive).start()
    else:
        loginGUI.cleanEntryLogin();
        loginGUI.login_head_label.config(text = ServerClient.ERROR_DATA)


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
    state = 0
    while state == 0:
        try:
            #quando viene chiamata la funzione receive, si mette in ascolto dei messaggi che arrivano sul socket
            msg = client.socket.recv(ServerClient.BUFSIZ).decode("utf8")
            chatGUI.insertMsgFromTextToChat(msg)    

            if(msg == Game.LOSE or msg == Game.END or  msg == ServerClient.KEY_QUIT_SERVE):
                sleep(5)
                state = 1;
                quitGame();

        except OSError:  
            break


# per uscire dalla partita
def quitGame():
    chatGUI.destroy();



def printTImer():

    end = 0;
    while end == 0:
        chatGUI.timer_label.config(text = str(timer.time))
        timer.decrTime()
        sleep(1)

        if(timer.time == 0):
            chatGUI.disabledButtons();
            msg = ServerClient.KEY_END_TIME + '\n\n'
            chatGUI.insertMsgFromTextToChat(msg)
            chatGUI.timer_label.config(text = str(timer.time))

            #tempo sara la parola chiave che il client manda al server per dire che ha finito il tempo
            client.socket.send(bytes(ServerClient.KEY_END_TIME, "utf8"))
            end = 1;


chatGUI.mainloop();
loginGUI.mainloop();