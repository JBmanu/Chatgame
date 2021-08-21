"""
@author: buizo
"""
import tkinter as tk

class UtilitiesGUI():
    HEADER_SERVER = "Server";
    TITLE_SERVER = "MASTER SERVER";

    START = "Start";
    STOP = "Stop";

    ADDRESS = "Address: ";
    ADDRESS_NONE = "Address: X.X.X.X ";

    PORT = "Port: ";
    PORT_NONE = "Port: XXXX "

    TITLE_LIST = "--------< Gamer List >--------";

    COLOR_LIGTH_GREEN = "#99ff99";
    COLOR_LIGTH_RED = "#ff8080";

    LOGIN_BG = "#BC8F8F"
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"
    BTN_COLOR = "#FF6347"

    FONT_H0 = ("Roman", 35, "bold", "italic");
    FONT_H1 = ("Italic", 16, "bold", "normal");
    FONT_H2 = ("Helvetica", 14, "bold");
    FONT_H3 = ("Helvetica", 13, "bold");
    FONT_H4 = ("Italic", 12, "bold", "normal");


    @staticmethod
    def configWindow(window, bg, dimensions):
        window.title(UtilitiesGUI.HEADER_SERVER)
        window.configure(bg = bg);
        window.geometry(dimensions);


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
    def linkDisplayScrollBar(display, scrollbar, height, width, bg, highBg, state):
        display.config(yscrollcommand = scrollbar.set, 
            height = height,
            width = width,
            background = bg,
            highlightbackground = highBg,
            state = state)