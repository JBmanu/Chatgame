"""
@author: buizo
"""

from View.UtilitiesView import UtilitiesVIew
import tkinter as tk

class ServerGUI(tk.Tk):

    def __init__(self):
        super().__init__();

        self.btnFrame = tk.Frame(self, width = 200, height = 100, bg ="white")
        self.infoFrame = tk.Frame(self, width = 200, height = 100, bg ="red")
        self.listFrame = tk.Frame(self, width = 200, height = 100)

        self.lbTitle = tk.Label();

        self.btnStart = tk.Button(self.btnFrame);
        self.btnStop = tk.Button(self.btnFrame);

        self.lblHost = tk.Label(self.infoFrame);
        self.lblPort = tk.Label(self.infoFrame);

        #self.lbLine = tk.Label();
        self.tkDisplay = tk.Text();
        #self.scrollBar = tk.Scrollbar();

        self.initializeWindow("400x500", "purple", "white");
        self.createTitle(UtilitiesVIew.TITLE_SERVER_GUI);
        self.createButtons();
        self.createViewIpAndPort();
        self.createListGamer();


    def getBtnStart(self):
        return self.btnStart;


    def getBtnStop(self):
        return self.btnStop;


    def initializeWindow(self, dimensions, colorBg, colorFg):
        self.title(UtilitiesVIew.HEADER_WINDOW);
        self.configure(bg = colorBg);
        self.geometry(dimensions);
        self.background = colorBg;
        self.foreground = colorFg;


    def createTitle(self, title):
        self.lbTitle.configure(
            text = title,
            font = UtilitiesVIew.FONT_TITLE, 
            bg = self.background, 
            fg = self.foreground);

        self.lbTitle.pack();

    def createButtons(self):
        self.btnStart.configure(
            text = UtilitiesVIew.START, 
            font = UtilitiesVIew.FONT, 
            bg = UtilitiesVIew.COLOR_LIGTH_GREEN,
            fg = self.foreground,
            activebackground = "green");
        self.btnStart.pack(side = tk.LEFT);

        self.btnStop.configure(
            text = UtilitiesVIew.STOP,  
            font = UtilitiesVIew.FONT, 
            bg = UtilitiesVIew.COLOR_LIGTH_RED,
            fg = self.foreground,
            activebackground = "red",
            state = tk.DISABLED);
        self.btnStop.pack(side = tk.LEFT);
      
    
    def createViewIpAndPort(self):

        self.lblHost.configure( 
            font = UtilitiesVIew.FONT, 
            text = UtilitiesVIew.ADDRESS + "X.X.X.X", 
            bg = self.background, 
            fg = self.foreground);
        self.lblHost.pack(side = tk.LEFT);
        
        self.lblPort.configure( 
            font = UtilitiesVIew.FONT, 
            text = UtilitiesVIew.PORT + "XXXX", 
            bg = self.background,  
            fg = self.foreground);
        self.lblPort.pack(side = tk.LEFT);
    

    def createListGamer(self):
        listClient = tk.Frame(self);
        
        lbLine = tk.Label(listClient, 
            font = UtilitiesVIew.FONT,
            text = UtilitiesVIew.TITLE_LIST).pack();

        self.tkDisplay.master = listClient;

        self.tkDisplay.configure(height = 20, width = 40);
        self.tkDisplay.pack(side = tk.LEFT, fill = tk.Y, padx = (5, 0));

        scrollBar = tk.Scrollbar(listClient);
        scrollBar.config(command = self.tkDisplay.yview);
        scrollBar.pack(side = tk.RIGHT, fill = tk.Y);

        self.tkDisplay.config(yscrollcommand = scrollBar.set, 
            background = "#F4F6F7", 
            highlightbackground = "grey", 
            state = "disabled");

        listClient.pack(side = tk.TOP, pady = (5, 10), fill = tk.Y);
