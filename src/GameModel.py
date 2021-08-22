"""
@author: buizo
"""
import os
from random import *

class GameModel():
    WELCOME = 'Info: Per uscire, scrivi -quit- \n\n'

    CHOICES = "Scegli tra a b c"

    CORRECT = "Corretto +1"
    WRONG = "Sbagliato -1"
    LOSE = "HAI PERSO"


    def __init__(self):
        self.choises = { 0 : "aA", 1 : "bB", 2 : "cC"};

        self.saluti = [];
        self.ruoli = []
        self.questionAnswer = {};

        self.playersRuolo = {};
        self.playersPoint = {};

        self.playersEndTIme = 0

        
    def readQuestionFromFile(self):
        # Ho usato path join per avere il path compatibili per piu S.O
        self.f = open(os.path.join("domande.txt"));

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


    def randomSaluti(self):
        return self.saluti[randint(0, len(self.saluti) - 1)];


    def randomRuolo(self):
        return self.ruoli[randint(0, len(self.ruoli) - 1)];


    def randomQuestion(self):
        listQuestion = []
        listQuestion.extend(self.questionAnswer.keys())
        return listQuestion[randint(0, len(listQuestion) - 1)]


    def inserChoiceLose(self, questions):
        questions[randint(0, 2)] = self.LOSE;
        print(questions)
        

    def questionForGame(self):
        questions = [self.randomQuestion(), self.randomQuestion(), self.randomQuestion()]
        self.inserChoiceLose(questions)

        return questions

    
    def incrPlayerEndTIme(self):
        self.playersEndTIme += 1;

    
    def allPlayersEndTIme(self):
        return self.playersEndTIme == (len(self.playersPoint))


    def winner(self):
        self.name = "manu";
        self.point = -999;

        for k, v in self.playersPoint.items():
            print("Controllo i punti dei giocatoriiiii")
            if(v > self.point):
                self.point = v;
                self.name = k
                print("controlloooo -> " + self.point)

        return (self.name, self.point)
            



   