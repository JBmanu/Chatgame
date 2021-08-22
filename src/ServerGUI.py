"""
@author: buizo
"""
from ServerModel import ServerModel
from UtilitiesGUI import UtilitiesGUI as Utility
import tkinter as tk


class ServerGUI(tk.Tk):
    
    def __init__(self):
        super().__init__();
        # creazione finestra server
        Utility.configWindow(self, Utility.GUI_BG, "400x500");

        # creazione del titolo della finestra del server
        titleFrame = tk.Frame(self).pack();
        Utility.createLabel(titleFrame, Utility.FONT_H0, Utility.TITLE_SERVER, Utility.GUI_BG, Utility.BG_COLOR).pack();

        # Creazione dei pulsanti per startare e fermare il server (btnStart, btnStop)
        btnFrame = tk.Frame(self);

        self.btnStart = Utility.createBtnStart(btnFrame, Utility.FONT_H1, Utility.START, Utility.COLOR_LIGTH_GREEN, Utility.BG_COLOR)
        self.btnStart.pack(side=tk.LEFT); 
        self.btnStop = Utility.createBtnStop(btnFrame, Utility.FONT_H1, Utility.STOP, Utility.COLOR_LIGTH_RED, Utility.BG_COLOR)
        self.btnStop.pack(side=tk.LEFT);
        btnFrame.pack(side=tk.TOP, pady=(5, 0))

        # Creazione di label per la visualizzazione address host e sulla porta
        infoFrame = tk.Frame(self)
        self.lblHost = Utility.createLabel(infoFrame, Utility.FONT_H1, Utility.ADDRESS_NONE,  Utility.GUI_BG, Utility.BG_COLOR)
        self.lblHost.pack(side=tk.LEFT);
        self.lblPort =  Utility.createLabel(infoFrame, Utility.FONT_H1, Utility.PORT_NONE,  Utility.GUI_BG, Utility.BG_COLOR)
        self.lblPort.pack(side=tk.LEFT);
        infoFrame.pack(side=tk.TOP, pady=(5, 0))

        # Il display client mostra l'area dove sono elencati i clients che partecipano al gioco
        listFrame = tk.Frame(self)
        Utility.createLabel(listFrame, Utility.FONT_H2, Utility.TITLE_LIST, "#F4F6F7", "black").pack()

        self.tkDisplay = tk.Text(listFrame, font = Utility.FONT_H4);
        self.tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0));

        scrollBar = tk.Scrollbar(listFrame, command = self.tkDisplay.yview)
        scrollBar.pack(side=tk.RIGHT, fill=tk.Y);

        Utility.linkDisplayScrollBar(self.tkDisplay, scrollBar, 20, 40, "#F4F6F7", "grey", "disabled");
        listFrame.pack(side=tk.BOTTOM, pady=(5, 10))


    """ funzione per l'attivazione del bottone start """
    def startBtns(self):
        self.btnStart.config(state=tk.DISABLED)
        self.btnStop.config(state=tk.NORMAL)
            
        self.lblHost.config(text = Utility.ADDRESS + ServerModel.ADDR)
        self.lblPort.config(text = Utility.PORT + str(ServerModel.PORT))


    """ funzione per l'attivazione del bottone stop """
    def stopBtns(self):
        self.btnStart.config(state=tk.NORMAL)
        self.btnStop.config(state=tk.DISABLED)
            
        self.lblHost.config(text = Utility.ADDRESS_NONE)
        self.lblPort.config(text = Utility.PORT_NONE)

    
    """ Funzione del l'aggiornamento dei dati dei client che si son connessi """
    def updateDisplay(self, gamers, ruoli):
        self.tkDisplay.config(state = tk.NORMAL)
        self.tkDisplay.delete('1.0', tk.END)

        for k, v in gamers.items():
            
            print(ruoli[k])
            text = "Points: " + str(v) + " => " + k + " - " + ruoli[k] + '\n';
            self.tkDisplay.insert(tk.END, text)

        self.tkDisplay.config(state=tk.DISABLED)