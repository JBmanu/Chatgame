"""
@author: buizo
"""
from random import choice
from GameModel import GameModel as Game
from ServerModel import ServerModel as Model
from ServerGUI import ServerGUI as GUI
from UtilitiesSC import UtilitiesSC as ServerClient
from threading import Thread


guiServer = GUI();
modelServer = Model();
gameModel = Game();

guiServer.btnStart.config(command = lambda : startServer());
guiServer.btnStop.config(command = lambda : stopServer());


""" Funzione che si attiva quando si preme il bottone start """
def startServer():
    gameModel.readQuestionFromFile();
    modelServer.openSocket();
    guiServer.startBtns();
    ACCEPT_THREAD = Thread(target = ecceptEntryConnection)
    ACCEPT_THREAD.start()


""" Funzione che si attiva quando si preme il bottone stop """
def stopServer():
    print("Stopping server")
    modelServer.closeServe();
    guiServer.stopBtns();
    guiServer.destroy();
    

""" La funzione che segue accetta le connessioni dei client in entrata."""
def ecceptEntryConnection():
    state = 0
    while state == 0:
        try:
            client, address = modelServer.server.accept()
        except OSError:
            state = 1


        # avvisa e salva il nickname del giocatore
        name = client.recv(ServerClient.BUFSIZ).decode("utf8")
        modelServer.sendEnterGameMsg(client, name)
        insertDataClientInGame(client, name, address)

        # al client che si connette per la prima volta fornisce alcune indicazioni di utilizzo
        modelServer.sendStringMsgToClient(client, gameModel.randomSaluti())
        modelServer.sendStringMsgToClient(client, Game.INFO + Game.RUOLO + gameModel.playersRuolo[name])
         
        Thread(target = manageClient, args = (client,)).start()


"""La funzione seguente gestisce la connessione di un singolo client per il gioco """
def manageClient(client): 
    state = 0
    questions = saveAndSendChoises(client);
    stateAnswer = 0
    questionChoice = ""

    while state == 0:
        try: 
            msg = client.recv(ServerClient.BUFSIZ)
            decodeMsg = msg.decode("utf8")
        
            if (msg == bytes(ServerClient.KEY_END_TIME, "utf8")):
                gameModel.incrPlayerEndTime();

                if (gameModel.isAllPlayersEndTime()):

                    winner = gameModel.findWinner();
                    modelServer.sendBroadcast(bytes(gameModel.generateMsgWinner(winner), "utf8"))
                    modelServer.sendBroadcast(bytes(Game.END, "utf8"))
                    modelServer.closeAllConnections();
                    break;
                    

            if (stateAnswer == 0):
                questionChoice = sendChoise(client, decodeMsg, questions);
                stateAnswer = 1
            else: 
                stateAnswer = 0
                sendWrongOrCorrect(client, questionChoice, decodeMsg)
                questions = saveAndSendChoises(client)
                questionChoice = ""
            
            if (msg == bytes(ServerClient.KEY_QUIT, "utf8") or questionChoice == Game.LOSE):
                modelServer.quitClient(client)
                gameModel.incrPlayerEndTime();
                break;
                
        except ConnectionResetError:
            state = 1


""" La funzione che manda la scelta del client """
def sendChoise(client, answer, questions):
    for k, v in gameModel.choises.items(): 
        if(answer < v):
            modelServer.sendStringMsgToClient(client, answer + ": " + questions[k])
            choice = questions[k]
            return choice


""" La funzione che manda la proposta delle scelte al client e ritorna la lista delle domande associate alle possibili scelte """
def saveAndSendChoises(client):
    modelServer.sendStringMsgToClient(client, (Model.HEADER + Game.CHOICES));
    return gameModel.questionForGame();


""" La funzione manda la stringa se la risposta e giusta o meno e assegna il punteggio """
def sendWrongOrCorrect(client, questionChoice, answer):
    if (questionChoice != "" and answer == gameModel.questionAnswer[questionChoice]):
        modelServer.sendStringMsgToClient(client, Game.CORRECT);
        gameModel.incrPlayerPoint(modelServer.sockets[client])
        
    elif(questionChoice != ""):
        modelServer.sendStringMsgToClient(client, Game.WRONG)
        gameModel.decrPlayerPoint(modelServer.sockets[client])

    guiServer.updateDisplay(gameModel.playersPoint, gameModel.playersRuolo)


""" La funzione inserisce i dati del client assegnadoli il punteggio, ruolo """
def insertDataClientInGame(client, name, address):
    modelServer.address[client] = address
    modelServer.sockets[client] = name
    gameModel.playersPoint[name] = 0;
    gameModel.playersRuolo[name] = gameModel.randomRuolo();

    guiServer.updateDisplay(gameModel.playersPoint, gameModel.playersRuolo)

        
guiServer.mainloop();