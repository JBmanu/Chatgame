from UtilitiesGUI import UtilitiesGUI as Utils
import tkinter as tk
from Timer import Timer 
from threading import Thread
from time import sleep

timer = Timer();

class ChatApplication(tk.Tk):
    
    def __init__(self):
        super().__init__();
        self.title("Chat Game")
        self.resizable(width = False, height = False)
        self.configure(width = 500, height = 550, bg = Utils.BG_COLOR)
        self.withdraw();
        
        #head label
        self.head_label = tk.Label(self, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                            text = "Benvenuto!", font = Utils.FONT_H3, pady = 10)
        self.head_label.place(relwidth = 0.875)
        
        #timer label
        self.timer_label = tk.Label(self, textvariable = timer.time, bg = Utils.BTN_COLOR, fg = Utils.TEXT_COLOR, font = Utils.FONT_H3)
        self.timer_label.place(relwidth = 0.14, relx = 0.875, relheight = 0.7)
        #qui ci ho passato nella label una textvariable dove dico la stringa timer.time, poi ho provato
        #senza stringa, ho provato tutto ma la label resta sempre vuota, mi sparo#
        
        #divisore
        self.line = tk.Label(self, width = 450, bg = Utils.BG_GRAY)
        self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        
        #label per widget di testo
        self.widget_label = tk.Label(self, width = 20, height = 2, bg = Utils.BG_COLOR)
        self.widget_label.place(relheight = 0.645, relwidth = 1, rely = 0.08)
        
        #widget di testo

        self.text_widget = tk.Text(self, width = 20, height = 2, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                                font = Utils.FONT_H4, padx = 5, pady = 5)

        self.text_widget.place(relheight = 0.645, relwidth = 0.975, rely = 0.08)
        self.text_widget.configure(cursor = "arrow", state = tk.DISABLED)
        # self.text_widget.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0));

        #barra di scorrimento
        self.scrollbar = tk.Scrollbar(self.widget_label)
        self.scrollbar.place(relheight = 1, relx = 0.974)

        self.scrollbar.configure(command = self.text_widget.yview)

        #label in basso
        self.bottom_label = tk.Label(self, bg = Utils.BG_GRAY, height = 80)
        self.bottom_label.place(relwidth = 1, rely = 0.825)
        
        #label per i tasti a, b e c
        self.under_label = tk.Label(self, height = 4, bg = Utils.BG_GRAY)
        self.under_label.place(relwidth = 1, rely = 0.723)
        
        
        #box inserimento testo
        self.msg_entry = tk.Entry(self.bottom_label, bg = "#2C3E50", fg = Utils.TEXT_COLOR, font = Utils.FONT_H2)
        self.msg_entry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus()
        
        # pulsante invio messaggio
        self.pulsante_invio = tk.Button(self.bottom_label, text = "Invia", font = Utils.FONT_H1, width = 20, bg = Utils.BG_GRAY)
        self.pulsante_invio.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)

        
        #pulsante a
        self.pulsante_a = tk.Button(self.under_label, text = "a", font = Utils.FONT_H1, width = 5, bg = Utils.BTN_COLOR)
        self.pulsante_a.place(relx = 0.03, rely = 0.2, relheight = 0.7, relwidth = 0.22)
        
        
        #pulsante b
        self.pulsante_b = tk.Button(self.under_label, text = "b", font = Utils.FONT_H1, width = 5, bg = Utils.BTN_COLOR)
        self.pulsante_b.place(relx = 0.26, rely = 0.2, relheight = 0.7, relwidth = 0.22)
        
        
        #pulsante c
        self.pulsante_c = tk.Button(self.under_label, text = "c", font = Utils.FONT_H1, width = 5, bg = Utils.BTN_COLOR)
        self.pulsante_c.place(relx = 0.49, rely = 0.2, relheight = 0.7, relwidth = 0.22)
        
        
        #pulsante quit
        self.pulsante_quit = tk.Button(self.under_label, text = "QUIT", font = Utils.FONT_H1, width = 4, bg = "#FF0000")
        self.pulsante_quit.place(relx = 0.85, rely = 0.1, relheight = 0.7, relwidth = 0.14)
        
        
        
    def _inserisci_messaggio(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, tk.END)
        msg1  =  f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor = "arrow", state = tk.NORMAL)
        self.text_widget.insert(tk.END, msg1)
        self.text_widget.configure(state = tk.DISABLED)
        self.msg_entry.delete(0, tk.END)


    def insertMsgFromTextToChat(self, msg):
        self.text_widget.configure(state = tk.NORMAL)
        self.text_widget.insert(tk.END, msg)
        self.text_widget.configure(state = tk.DISABLED)

    
    def disabledButtons(self):
        self.pulsante_invio.config(state = tk.DISABLED)
        self.pulsante_a.config(state = tk.DISABLED)
        self.pulsante_b.config(state = tk.DISABLED)
        self.pulsante_c.config(state = tk.DISABLED)