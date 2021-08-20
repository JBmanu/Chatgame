from Utilities import Utilities as Utils
import tkinter as tk

class ChatApplication(tk.Tk):
    
    def __init__(self):
        super().__init__();
        self.title("Chat Game")
        self.resizable(width = False, height = False)
        self.configure(width = 500, height = 550, bg = Utils.BG_COLOR)
        self.withdraw();
        
        #head label
        self.head_label = tk.Label(self, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                            text = "Benvenuto!", font = Utils.FONT_BOLD, pady = 10)
        self.head_label.place(relwidth = 1)
        
        #divisore
        self.line = tk.Label(self, width = 450, bg = Utils.BG_GRAY)
        self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        
        #widget di testo
        self.text_widget = tk.Text(self, width = 20, height = 2, bg = Utils.BG_COLOR, fg = Utils.TEXT_COLOR,
                                font = Utils.FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.645, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor = "arrow", state = tk.DISABLED)
        
        #barra di scorrimento
        self.scrollbar = tk.Scrollbar(self.text_widget)
        self.scrollbar.place(relheight = 1, relx = 0.974)
        self.scrollbar.configure(command = self.text_widget.yview)
        
        #label in basso
        self.bottom_label = tk.Label(self, bg = Utils.BG_GRAY, height = 80)
        self.bottom_label.place(relwidth = 1, rely = 0.825)
        
        #label per i tasti a, b e c
        self.under_label = tk.Label(self, height = 4, bg = Utils.BG_GRAY)
        self.under_label.place(relwidth = 1, rely = 0.723)
        
        
        #box inserimento testo
        self.msg_entry = tk.Entry(self.bottom_label, bg = "#2C3E50", fg = Utils.TEXT_COLOR, font = Utils.FONT)
        self.msg_entry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._premere_enter)
        
        # pulsante invio messaggio
        self.pulsante_invio = tk.Button(self.bottom_label, text = "Invia", font = Utils.FONT_BOLD, width = 20, bg = Utils.BG_GRAY,
                                command = lambda: self._premere_enter(None))
        self.pulsante_invio.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)
        
        #pulsante a
        self.pulsante_a = tk.Button(self.under_label, text = "a", font = Utils.FONT_BUTTON, width = 5, bg = Utils.BUTTON_COLOR,
                            command = lambda: self._premere_Char("a"))
        self.pulsante_a.place(relx = 0.1, rely = 0.2, relheight = 0.7, relwidth = 0.22)
        
        
        #pulsante b
        self.pulsante_b = tk.Button(self.under_label, text = "b", font = Utils.FONT_BUTTON, width = 5, bg = Utils.BUTTON_COLOR,
                            command = lambda: self._premere_Char("b"))
        self.pulsante_b.place(relx = 0.39, rely = 0.2, relheight = 0.7, relwidth = 0.22)
        
        
        #pulsante c
        self.pulsante_c = tk.Button(self.under_label, text = "c", font = Utils.FONT_BUTTON, width = 5, bg = Utils.BUTTON_COLOR,
                            command = lambda: self._premere_Char("c"))
        self.pulsante_c.place(relx = 0.68, rely = 0.2, relheight = 0.7, relwidth = 0.22)
        
        
    def _premere_Char(self, char):
        self._inserisci_messaggio(char, "Tu")
        
    
    def _premere_enter(self, event):
        msg  =  self.msg_entry.get()
        self._inserisci_messaggio(msg, "Tu")
        
        
    def _inserisci_messaggio(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, tk.END)
        msg1  =  f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor = "arrow", state = tk.NORMAL)
        self.text_widget.insert(tk.END, msg1)
        self.text_widget.configure(state = tk.DISABLED)
