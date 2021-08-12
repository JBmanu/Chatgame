"""
Created on Tue Aug 10 14:41:22 2021

@author: buizo
"""

from View.ServerGUI import ServerGUI
import tkinter as tk

import socket
import threading
from time import sleep

gui = ServerGUI("purple", "white");
gui.initializeWindow("400x500");
gui.createTitle("MASTER SERVER");
gui.createButtons();
gui.createViewIpAndPort();
gui.createListGamer();

gui.window.mainloop()