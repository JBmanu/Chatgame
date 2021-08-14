"""
@author: buizo
"""

from View.UtilitiesView import UtilitiesVIew
import tkinter as tk

class ServerGUI():

    def __init__(self):
        self.window = tk.Tk();
        self.lbTitle = tk.Label();
        self.btnStart = tk.Button();
        self.btnStop = tk.Button();

        self.lblHost = tk.Label();
        self.lblPort = tk.Label();

        #self.lbLine = tk.Label();
        #self.tkDisplay = tk.Text();
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
        self.window.title(UtilitiesVIew.HEADER_WINDOW);
        self.window.configure(bg = colorBg);
        self.window.geometry(dimensions);
        self.background = colorBg;
        self.foreground = colorFg;


    def createTitle(self, title):
        titleCanvas = tk.Frame(self.window);

        self.lbTitle.master = titleCanvas;
        self.lbTitle.configure(
            text = title,
            font = UtilitiesVIew.FONT_TITLE, 
            bg = self.background, 
            fg = self.foreground);

        self.lbTitle.pack();

        titleCanvas.pack(side = tk.TOP, pady = (5, 0)); 
        

    def createButtons(self):
        btnCanvas = tk.Frame(self.window);

        self.btnStart.master = btnCanvas;
        self.btnStart.configure(
            text = UtilitiesVIew.START, 
            font = UtilitiesVIew.FONT, 
            bg = UtilitiesVIew.COLOR_LIGTH_GREEN,
            fg = self.foreground,
            activebackground = "green");

        self.btnStart.pack(side = tk.LEFT);

        self.btnStop.master = btnCanvas;
        self.btnStop.configure(
            text = UtilitiesVIew.STOP,  
            font = UtilitiesVIew.FONT, 
            bg = UtilitiesVIew.COLOR_LIGTH_RED,
            fg = self.foreground,
            activebackground = "red",
            state = tk.DISABLED);
            
        self.btnStop.pack(side = tk.LEFT);

        btnCanvas.pack(side = tk.TOP, pady = (5, 0));

    
    def createViewIpAndPort(self):
        middleCanvas = tk.Frame(self.window);

        self.lblHost.master = middleCanvas;
        self.lblHost.configure( 
            font = UtilitiesVIew.FONT, 
            text = UtilitiesVIew.ADDRESS + "X.X.X.X", 
            bg = self.background, 
            fg = self.foreground);
        self.lblHost.pack(side = tk.LEFT);

        self.lblPort.master = middleCanvas;
        self.lblPort.configure( 
            font = UtilitiesVIew.FONT, 
            text = UtilitiesVIew.PORT + "XXXX", 
            bg = self.background,  
            fg = self.foreground);
        self.lblPort.pack(side = tk.LEFT);

        middleCanvas.pack(side = tk.TOP, pady = (5, 0));
    

    def createListGamer(self):
        listClient = tk.Frame(self.window);
        
        self.lbLine = tk.Label(listClient, 
            font = UtilitiesVIew.FONT,
            text = UtilitiesVIew.TITLE_LIST).pack();

        self.tkDisplay = tk.Text(listClient, height = 20, width = 40);
        self.tkDisplay.pack(side = tk.LEFT, fill = tk.Y, padx = (5, 0));

        scrollBar = tk.Scrollbar(listClient);
        scrollBar.config(command = self.tkDisplay.yview);
        scrollBar.pack(side = tk.RIGHT, fill = tk.Y);

        self.tkDisplay.config(yscrollcommand = scrollBar.set, 
            background = "#F4F6F7", 
            highlightbackground = "grey", 
            state = "disabled");

        listClient.pack(side = tk.TOP, pady = (5, 10));
