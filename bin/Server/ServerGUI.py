"""
@author: buizo
"""
from ServerModel import ServerModel
from Utilities import Utilities as Utility
import tkinter as tk


class ServerGUI(tk.Tk):
    
    def __init__(self):
        super().__init__();
        # creazione finestra server
        Utility.configWindow(self, "purple", "400x500");

        # creazione del titolo della finestra del server
        titleFrame = tk.Frame(self).pack();
        Utility.createTitle(titleFrame, Utility.FONT_TITLE, Utility.TITLE_SERVER_GUI, "purple", "white").pack();

        # Creazione dei pulsanti per startare e fermare il server (btnStart, btnStop)
        btnFrame = tk.Frame(self);

        self.btnStart = Utility.createBtnStart(btnFrame, Utility.FONT, Utility.START, Utility.COLOR_LIGTH_GREEN, "white")
        self.btnStart.pack(side=tk.LEFT); 
        self.btnStop = Utility.createBtnStop(btnFrame, Utility.FONT, Utility.STOP, Utility.COLOR_LIGTH_RED, "white")
        self.btnStop.pack(side=tk.LEFT);
        btnFrame.pack(side=tk.TOP, pady=(5, 0))

        # Creazione di label per la visualizzazione address host e sulla porta
        infoFrame = tk.Frame(self)
        self.lblHost = Utility.createLabel(infoFrame, Utility.FONT, Utility.ADDRESS_NONE, "purple", "white")
        self.lblHost.pack(side=tk.LEFT);
        self.lblPort =  Utility.createLabel(infoFrame, Utility.FONT, Utility.PORT_NONE, "purple", "white")
        self.lblPort.pack(side=tk.LEFT);
        infoFrame.pack(side=tk.TOP, pady=(5, 0))

        # Il display client mostra l'area dove sono elencati i clients che partecipano al gioco
        listFrame = tk.Frame(self)
        Utility.createLabel(listFrame, Utility.FONT, Utility.TITLE_LIST, "#F4F6F7", "black").pack()

        self.tkDisplay = tk.Text(listFrame, font = Utility.FONT1);
        self.tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0));

        scrollBar = tk.Scrollbar(listFrame, command = self.tkDisplay.yview)
        scrollBar.pack(side=tk.RIGHT, fill=tk.Y);

        Utility.unionDisplayWitchScrollBar(self.tkDisplay, scrollBar, 20, 40, "#F4F6F7", "grey", "disabled");
        


    def startBtns(self):
        self.btnStart.config(state=tk.DISABLED)
        self.btnStop.config(state=tk.NORMAL)
            
        self.lblHost.config(text = Utility.ADDRESS + ServerModel.HOST_ADDR)
        self.lblPort.config(text = Utility.PORT + str(ServerModel.HOST_PORT))

    
    def stopBtns(self):
        self.btnStart.config(state=tk.NORMAL)
        self.btnStop.config(state=tk.DISABLED)
            
        self.lblHost.config(text = Utility.ADDRESS_NONE)
        self.lblPort.config(text = Utility.PORT_NONE)

    
    def updateDisplay(self, gamers, ruoli):
        self.tkDisplay.config(state = tk.NORMAL)
        self.tkDisplay.delete('1.0', tk.END)

        for k, v in gamers.items():
            
            print(ruoli[k])
            text = ruoli[k] + " => " + k + " " + str(v);
            self.tkDisplay.insert(tk.END, text + "\n")

        self.tkDisplay.config(state=tk.DISABLED)