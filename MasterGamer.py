# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:41:22 2021

@author: buizo
"""

import tkinter as tk
from tkinter.font import BOLD, Font

import socket
import threading
from time import sleep

# Create GUI for server
window = tk.Tk();
window.title("Server");

# Create cavas for Title
titleCanvas = tk.Frame(window);

lbLine = tk.Label(titleCanvas, text = "MASTER SERVER", font = ("Arial", 20)).pack();
titleCanvas.pack(side = tk.TOP, pady = (5, 0));

# Create canvas for buttons
btnCanvas = tk.Frame(window);
btnStart = tk.Button(btnCanvas, text = "Start", command = lambda : start_server());
btnStart.pack(side = tk.LEFT);

btnStop = tk.Button(btnCanvas, text = "Stop", command = lambda : stop_server(), state = tk.DISABLED);
btnStop.pack(side = tk.LEFT);

btnCanvas.pack(side = tk.TOP, pady = (5, 0));

# Create canvar for IP and Port of server
middleCanvas = tk.Frame(window);

lblHost = tk.Label(middleCanvas, text = "Address: X.X.X.X");
lblHost.pack(side = tk.LEFT);

lblPort = tk.Label(middleCanvas, text = "Port: XXXX");
lblPort.pack(side = tk.LEFT);

middleCanvas.pack(side = tk.TOP, pady = (5, 0));

# Create list for gamers that connect to server
listClient = tk.Frame(window);
lbLine = tk.Label(listClient, text = "**********Gamer List**********").pack();

scrollBar = tk.Scrollbar(listClient);
scrollBar.pack(side = tk.RIGHT, fill = tk.Y);

tkDisplay = tk.Text(listClient, height = 10, width = 30);
tkDisplay.pack(side = tk.LEFT, fill = tk.Y, padx = (5, 0));
scrollBar.config(command = tkDisplay.yview);
tkDisplay.config(yscrollcommand = scrollBar.set, background = "#F4F6F7", highlightbackground = "grey", state = "disabled");

listClient.pack(side = tk.BOTTOM, pady = (5, 10));



def start_server() : {
        
}

def stop_server() : {
        
}

window.mainloop()