
from Model.ServerModel import ServerModel
from View.ServerGUI import ServerGUI
from MasterServer import MasterServer



gui = ServerGUI();

print(gui.window);

print(gui.lbTitle);

print(gui.btnStop)


gui.window.mainloop();