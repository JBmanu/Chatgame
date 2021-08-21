"""
@author: buizo
"""
from random import choice
from GameModel import GameModel as Game
from ServerModel import ServerModel as Model
from ServerGUI import ServerGUI as GUI
from threading import Thread

guiServer = GUI();
modelServer = Model();
gameModel = Game();

guiServer.btnStart.config(command = lambda : startServer());
guiServer.btnStop.config(command = lambda : stopServer());


def startServer():
    gameModel.readQuestionFromFile();
    modelServer.openSocket();
    guiServer.startBtns();
    ACCEPT_THREAD = Thread(target=accetta_connessioni_in_entrata)
    ACCEPT_THREAD.start()


def stopServer():
    print("Stopping server")
    modelServer.server.close();
    guiServer.stopBtns();
    

""" La funzione che segue accetta le connessioni  dei client in entrata."""
def accetta_connessioni_in_entrata():
    while True:
        # Accetto connessione e salvo indirizzo
        client, client_address = modelServer.server.accept()
        modelServer.address[client] = client_address

        # avvisa e salva il nickname del giocatore
        name = client.recv(Model.BUFSIZ).decode("utf8")
        msg = "%s si è unito al gioco!" % name
        sendBroadcastWithout(client, bytes(msg, "utf8"))
        insertDataClient(client, name)

        # al client che si connette per la prima volta fornisce alcune indicazioni di utilizzo
        client.send(bytes(gameModel.randomSaluti(), "utf8"))
        client.send(bytes(Game.WELCOME + "Il tuo ruolo sara => " + gameModel.playersRuolo[name] , "utf8"))
         
        Thread(target = gestice_client, args = (client,)).start()


"""La funzione seguente gestisce la connessione di un singolo client."""
def gestice_client(client):  # Prende il socket del client come argomento della funzione.

    questions = saveAndSendChoise(client);
    stateAnswer = 0
    questionChoice = ""

    #si mette in ascolto del thread del singolo client e ne gestisce l'invio dei messaggi o l'uscita dalla Chat
    while True:
        msg = client.recv(Model.BUFSIZ)
        answer = msg.decode("utf8") 

        if (stateAnswer == 0):
            questionChoice = actionChoise(client, answer, questions);
            stateAnswer = 1
        else: 
            stateAnswer = 0
            sendWrongOrCorrect(client, questionChoice, answer)
            questions = saveAndSendChoise(client)
            questionChoice = ""
        
        if (msg == bytes("quit", "utf8") or questionChoice == Game.LOSE):
            clientQuit(client, modelServer.clients[client])
            break;


""" La funzione, che segue, invia un messaggio in broadcast a tutti i client."""
def sendBroadcastToClients(msg, prefisso=""):  # il prefisso è usato per l'identificazione del nome.
    for utente in modelServer.clients:
        utente.send(bytes(prefisso, "utf8")+msg)


def sendBroadcastWithout(client, msg, prefisso=""):
    for utente in modelServer.clients:
        if (utente != client):
            utente.send(bytes(prefisso, "utf8")+msg)


def clientQuit(client, nome):
    sendBroadcastToClients(bytes("%s ci lascia, ha perso \n" % nome, "utf8"))
    del modelServer.clients[client]
    #elimino solo la connession ma non il dizionazio dei giocatori perche serve per il punteggio
    guiServer.updateDisplay(gameModel.playersPoint, gameModel.playersRuolo)
    client.close()


def actionChoise(client, answer, questions):
    for k, v in gameModel.choises.items(): 
        if(answer < v):
            client.send(bytes(answer + ": " + questions[k], "utf8"))
            choice = questions[k]
            return choice


def saveAndSendChoise(client):
    client.send(bytes((Model.HEADER + Game.CHOICES + '\n'), "utf8"))
    return gameModel.questionForGame();


def sendWrongOrCorrect(client, questionChoice, answer):
    if (questionChoice != "" and answer == gameModel.questionAnswer[questionChoice]):
        client.send(bytes(Game.CORRECT + "\n", "utf8"))
        gameModel.playersPoint[modelServer.clients[client]] += 1
        guiServer.updateDisplay(gameModel.playersPoint, gameModel.playersRuolo)
        
    elif(questionChoice != ""):
        client.send(bytes(Game.WRONG + "\n", "utf8"))
        gameModel.playersPoint[modelServer.clients[client]] -= 1
        guiServer.updateDisplay(gameModel.playersPoint, gameModel.playersRuolo)


def insertDataClient(client, name):
    modelServer.clients[client] = name
    gameModel.playersPoint[name] = 0;
    gameModel.playersRuolo[name] = gameModel.randomRuolo();

    guiServer.updateDisplay(gameModel.playersPoint, gameModel.playersRuolo)

        
guiServer.mainloop();