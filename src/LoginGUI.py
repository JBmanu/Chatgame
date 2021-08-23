from ServerModel import ServerModel
from UtilitiesGUI import UtilitiesGUI as Utils
import tkinter as tk

class LoginApplication(tk.Tk):
    
    def __init__(self):
        super().__init__();
        self.title("Login")
        self.resizable(width = False, height = False)
        self.configure(width = 500, height = 350, bg = Utils.GUI_BG)
        
        
        #head label
        self.login_head_label = tk.Label(self, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                                 text = "Inserisci le credenziali richieste per accedere:", font = Utils.FONT_H3, pady = 1)
        self.login_head_label.place(relwidth = 1)
        
        #divisore
        self.line2 = tk.Label(self, width = 450, bg = Utils.BG_GRAY)
        self.line2.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        
        #label HOST
        self.ip_label = tk.Label(self, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR, 
                         text = "HOST:", font = Utils.FONT_H3, padx = 1, pady = 10)
        self.ip_label.place(relwidth = 0.2, rely = 0.15)
        
        
        self.ip_label_fianco = tk.Label(self, height =  3, bg = Utils.BG_COLOR)
        self.ip_label_fianco.place(relwidth = 0.7, relx = 0.25, rely = 0.137)
        
        #label PORT
        self.port_label = tk.Label(self, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                           text = "PORT:", font = Utils.FONT_H3, padx = 1, pady = 10)
        self.port_label.place(relwidth = 0.2, rely = 0.35)
        
        self.port_label_fianco = tk.Label(self, height =  3, bg = Utils.BG_COLOR)
        self.port_label_fianco.place(relwidth = 0.7, relx = 0.25, rely = 0.34)
        
        #label nickname
        self.nick_label = tk.Label(self, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                           text = "Nickname:", font = Utils.FONT_H3, padx = 1, pady = 10)
        self.nick_label.place(relwidth = 0.2, rely = 0.6)
        
        self.nick_label_fianco = tk.Label(self, height =  3, bg = Utils.BG_COLOR)
        self.nick_label_fianco.place(relwidth = 0.7, relx = 0.25, rely = 0.585)
        
        #label pulsante login credenziale
        self.pulsante_login_label = tk.Label(self, height = 3, bg = Utils.GUI_BG)
        self.pulsante_login_label.place(relwidth = 1, rely = 0.825)
        
        #pulsante login
        self.pulsante_login = tk.Button(self.pulsante_login_label, text = "Login", font = Utils.FONT_H2, width = 5, bg = Utils.BTN_COLOR)
        self.pulsante_login.place(relx = 0.39, relheight = 1, relwidth = 0.22)
        
        #pulsante autocompletamento
        self.pulsante_riempimento = tk.Button(self.pulsante_login_label, text = "AUTO", font = Utils.FONT_H4, width = 3, bg = Utils.BG_GRAY, 
            command = lambda : self.autoCompile())
        self.pulsante_riempimento.place(relx = 0.65, relheight = 0.850, relwidth = 0.13)

        #box inserimento testo HOST
        self.host_entry  =  tk.Entry(self.ip_label_fianco, bg = "#2C3E50", fg = Utils.TEXT_COLOR, font = Utils.FONT_H2)
        self.host_entry.place(relwidth = 1, relheight = 1, rely = 0.008, relx = 0.011)
        self.host_entry.focus()
        
        
         #box inserimento testo PORT
        self.port_entry  =  tk.Entry(self.port_label_fianco, bg = "#2C3E50", fg = Utils.TEXT_COLOR, font = Utils.FONT_H2)
        self.port_entry.place(relwidth = 1, relheight = 1, rely = 0.008, relx = 0.011)
        self.port_entry.focus()
     
        #box inserimento testo NICK
        self.nick_entry  =  tk.Entry(self.nick_label_fianco, bg = "#2C3E50", fg = Utils.TEXT_COLOR, font = Utils.FONT_H2)
        self.nick_entry.place(relwidth = 1, relheight = 1, rely = 0.008, relx = 0.011)
        self.nick_entry.focus()

    
    def cleanEntryLogin(self):
        self.host_entry.delete(0, tk.END)
        self.port_entry.delete(0, tk.END)
        self.nick_entry.delete(0, tk.END)


    def autoCompile(self):
        self.host_entry.insert(tk.END, ServerModel.ADDR)
        self.port_entry.insert(tk.END, str(ServerModel.PORT))
        self.nick_entry.insert(tk.END, "user")