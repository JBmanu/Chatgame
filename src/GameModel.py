"""
@author: buizo
"""
import os
from random import *

class GameModel():
    INFO = 'Info: Per uscire, scrivi -quit- \n\n'
    RUOLO = "Il tuo ruolo sara => "

    CHOICES = "Scegli tra a b c"

    CORRECT = "Corretto +1"
    WRONG = "Sbagliato -1"
    LOSE = "HAI PERSO"

    END = "FINE..."

    FILE = os.path.join("domande.txt")

    def __init__(self):
        self.choises = { 0 : "aA", 1 : "bB", 2 : "cC"};

        self.saluti = [];
        self.ruoli = []
        self.questionAnswer = {};

        self.playersRuolo = {};
        self.playersPoint = {};

        self.playersEndTime = 0

    """ Legge il file per avere le stringhe di: saluto, ruolo, domanda-risposta """
    def readQuestionFromFile(self):
        self.f = open(self.FILE);

        for line in self.f.readlines():
            splitString = line.split(" -> ");

            if("\n" not in splitString):
                if(splitString[0] == "saluto"):
                    self.saluti.append(splitString[1])
                elif(splitString[0] == "ruolo"):
                    self.ruoli.append(splitString[1])
                else:
                    chars = list(splitString[2])
                    chars.remove('\n');
                    splitString[2] = "".join(chars);
                    self.questionAnswer[splitString[1]] = splitString[2];
        
        self.f.close();


    """ Ritorna un saluto random """
    def randomSaluti(self):
        return self.saluti[randint(0, len(self.saluti) - 1)];


    """ Ritorna un ruolo random """
    def randomRuolo(self):
        return self.ruoli[randint(0, len(self.ruoli) - 1)];


    """ Ritorna una domanda random """
    def randomQuestion(self):
        listQuestion = []
        listQuestion.extend(self.questionAnswer.keys())
        return listQuestion[randint(0, len(listQuestion) - 1)]


    """ In una lista di domande ne cambia una il HAI PERSO """
    def inserChoiceLose(self, questions):
        questions[randint(0, 2)] = self.LOSE;
        print(questions)
        

    """ Genera una lista con di domande per il gioco """
    def questionForGame(self):
        questions = [self.randomQuestion(), self.randomQuestion(), self.randomQuestion()]
        self.inserChoiceLose(questions)

        return questions

    
    """ Incrementa i giocatori che hanno finito il tempo """
    def incrPlayerEndTime(self):
        self.playersEndTime += 1;

    
    """ Ritorna se tutti i giocatori hanno finito il tempo"""
    def isAllPlayersEndTime(self):
        lenghPlayers = len(self.playersPoint)
        return self.playersEndTime == lenghPlayers


    """ Funnzion che ritorna una tupla del giocatore che ha vinto e i punti"""
    def findWinner(self):
        self.name = "manu";
        self.point = -999;

        for k, v in self.playersPoint.items():
            if(v > self.point):
                self.point = v;
                self.name = k

        return (self.name, self.point)
            
            
    """ Genera il messaggio da inviare ai giocatori di chi ha vinto """
    def generateMsgWinner(self, winner):
        return "Ha vinto: " + winner[0] + " con " + str(winner[1]) + " punti\n\n"

    
    """ Incrementa di un il punteggio di un giocatore """
    def incrPlayerPoint(self, name):
        self.playersPoint[name] += 1

    
    """ Decrementa di un il punteggio di un giocatore """
    def decrPlayerPoint(self, name):
        self.playersPoint[name] -= 1