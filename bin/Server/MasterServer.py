"""
@author: buizo
"""
from ServerModel import ServerModel as Model
from ServerGUI import ServerGUI as GUI

guiServer = GUI();
modelServer = Model();

guiServer.btnStart.config(command = lambda : startServer());
guiServer.btnStop.config(command = lambda : stopServer());


def startServer():
    modelServer.initServer();
    guiServer.startBtns()


def stopServer():
    modelServer.server = None;
    guiServer.stopBtns();
    

guiServer.mainloop();