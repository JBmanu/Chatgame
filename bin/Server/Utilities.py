"""
@author: buizo
"""
import tkinter as tk

class Utilities():
    HEADER_WINDOW = "Server";
    TITLE_SERVER_GUI = "MASTER SERVER";

    START = "Start";
    STOP = "Stop";

    ADDRESS = "Address: ";
    ADDRESS_NONE = "Address: X.X.X.X ";

    PORT = "Port: ";
    PORT_NONE = "Port: XXXX "

    TITLE_LIST = "--------< Gamer List >--------";

    COLOR_LIGTH_GREEN = "#99ff99";
    COLOR_LIGTH_RED = "#ff8080";

    FONT_TITLE = ("Roman", 35, "bold", "italic");
    FONT = ("Italic", 16, "bold", "normal");
    FONT1 = ("Italic", 12, "bold", "normal");




    @staticmethod
    def configWindow(window, bg, dimensions):
        window.title(Utilities.HEADER_WINDOW)
        window.configure(bg = bg);
        window.geometry(dimensions);


    @staticmethod
    def createTitle(frame, font, text, bg, fg, ):
        return tk.Label(frame, 
            font = font,
            text = text, 
            bg = bg,
            fg = fg);


    @staticmethod 
    def createBtnStart(btnFrame, font, text, bg, fg):
        return tk.Button(btnFrame, 
            font = font,
            text = text, 
            bg = bg,    
            fg = fg, 
            activebackground = "green");
    

    @staticmethod 
    def createBtnStop(btnFrame, font, text, bg, fg):
        return tk.Button(btnFrame, 
            font = font,
            text = text, 
            bg = bg,    
            fg = fg, 
            activebackground = "red",
            state = tk.DISABLED); 


    @staticmethod
    def createLabel(infoFrame, font, text, bg, fg):
        return tk.Label(infoFrame,
            font = font,
            text = text,
            bg = bg, 
            fg = fg);   


    @staticmethod
    def unionDisplayWitchScrollBar(display, scrollbar, height, width, bg, highBg, state):
        display.config(yscrollcommand = scrollbar.set, 
            height = height,
            width = width,
            background = bg,
            highlightbackground = highBg,
            state = state)


    @staticmethod
    def update_client_names_display(nameList, display):
        display.config(state=tk.NORMAL)
        display.delete('1.0', tk.END)

        for c in nameList:
            display.insert(tk.END, c.decode()+"\n")
            display.config(state=tk.DISABLED)