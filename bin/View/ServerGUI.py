"""
Created on Tue Aug 10 14:41:22 2021

@author: buizo
"""

import tkinter as tk

class ServerGUI:
    COST_HEADER_WINDOW = "Server";

    COST_START = "Start";
    COST_STOP = "Stop";

    COST_COLOR_LIGTH_GREEN = "#99ff99";
    COST_COLOR_LIGTH_RED = "#ff8080";

    COST_FONT_TITLE = ("Roman", 35, "bold", "italic");
    COST_FONT = ("Italic", 16, "bold", "normal");

    def __init__(self, colorBg, colorFg):
        self.window = tk.Tk();
        self.background = colorBg;
        self.foreground = colorFg;
        self.window.configure(bg = self.background);


    def initializeWindow(self, dimensions):
        self.window.title(self.COST_HEADER_WINDOW);
        self.window.geometry(dimensions);


    def createTitle(self, title):
        titleCanvas = tk.Frame(self.window);

        self.lbTitle = tk.Label(
            titleCanvas, text = title, 
            font = self.COST_FONT_TITLE, 
            bg = self.background, 
            fg = self.foreground).pack();

        titleCanvas.pack(side = tk.TOP, pady = (5, 0)); 
        

    def createButtons(self):
        btnCanvas = tk.Frame(self.window);

        self.btnStart = tk.Button(btnCanvas, 
            text = self.COST_START, 
            font = self.COST_FONT, 
            bg = self.COST_COLOR_LIGTH_GREEN,
            fg = self.foreground,
            activebackground = "green",
            ).pack(side = tk.LEFT);

        self.btnStop = tk.Button(btnCanvas, 
            text = self.COST_STOP,  
            font = self.COST_FONT, 
            bg = self.COST_COLOR_LIGTH_RED,
            fg = self.foreground,
            activebackground = "red"
            ).pack(side = tk.LEFT);

        btnCanvas.pack(side = tk.TOP, pady = (5, 0));

    
    def createViewIpAndPort(self):
        middleCanvas = tk.Frame(self.window);

        self.lblHost = tk.Label(middleCanvas, 
            font = self.COST_FONT, 
            text = "Address: X.X.X.X", 
            bg = self.background, 
            fg = self.foreground
            ).pack(side = tk.LEFT);

        self.lblPort = tk.Label(middleCanvas, 
            font = self.COST_FONT, 
            text = "Port: XXXX", 
            bg = self.background,  
            fg = self.foreground
            ).pack(side = tk.LEFT);

        middleCanvas.pack(side = tk.TOP, pady = (5, 0));
    

    def createListGamer(self):
        listClient = tk.Frame(self.window);
        
        self.lbLine = tk.Label(listClient, 
            font = self.COST_FONT,
            text = "--------< Gamer List >--------").pack();

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
