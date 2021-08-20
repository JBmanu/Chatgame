# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:52:18 2021

@author: sabat
"""

from tkinter import *
import tkinter as tk
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from time import sleep

LOGIN_BG = "#BC8F8F"
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
BUTTON_COLOR = "#FF6347"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
FONT_BUTTON = "Helvetica 13 bold"



class ClientToServer:
    
    def connect_to_server(name):
        global client, HOST, PORT, NICK
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, PORT))
            client.send(name.encode()) # Invia il nome al server dopo la connessione
    
            # disable widgets
            btn_connect.config(state=tk.DISABLED)
            ent_name.config(state=tk.DISABLED)
            lbl_name.config(state=tk.DISABLED)
            enable_disable_buttons("disable")
    
            # avvia un thread per continuare a ricevere messaggi dal server
            # non bloccare il thread principale :)
            threading._start_new_thread(receive_message_from_server, (client, "m"))
        except Exception as e:
            login_head_label.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST + " on port: " + str(PORT) + " Server may be Unavailable. Try again later")


    
    def receive():
        while True:
            try:
                #quando viene chiamata la funzione receive, si mette in ascolto dei messaggi che
                #arrivano sul socket
                msg = client_socket.recv(BUFSIZ).decode("utf8")
                #visualizziamo l'elenco dei messaggi sullo schermo
                #e facciamo in modo che il cursore sia visibile al termine degli stessi
                self.text_widget.insert(END, msg)
                # Nel caso di errore e' probabile che il client abbia abbandonato la chat.
            except OSError:  
                break

#invio messaggi
    def send(event=None):
        # invia il messaggio sul socket
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            self.window.quit()

#funzione invocata a chiusura chat
    def on_closing(event=None):
            msg.set("{quit}")
            send()
            



client = None
HOST = '127.0.0.1'
PORT = 8080    

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target = receive)
receive_thread.start()    


def connect():
    global NICK
    if len(self.nick_entry.get()) < 1:
        login_head_label.showerror(text="Inserisci un nickname valido! <es: Bobby92>")
    else:
        NICK = self.nick_entry.get()
        connect_to_server(NICK)

           

class LoginApplication:
    
    def __init__(self):
        self.login_window = Tk()
        self._setup_login_window()
        
    def run(self):
        self.login_window.mainloop()
        
    def _setup_login_window(self):
        self.login_window.title("Login")
        self.login_window.resizable(width=False, height=False)
        self.login_window.configure(width= 500, height= 350, bg=LOGIN_BG)
        
        
        #head label
        login_head_label = Label(self.login_window, bg=BG_COLOR, fg=TEXT_COLOR,
                                 text="Inserisci le credenziali richieste per accedere:", font=FONT_BOLD, pady=1)
        login_head_label.place(relwidth=1)
        
        
        #divisore
        line2 = Label(self.login_window, width=450, bg=BG_GRAY)
        line2.place(relwidth=1, rely=0.07, relheight=0.012)
        
        #label HOST
        ip_label = Label(self.login_window, bg=BG_COLOR, fg=TEXT_COLOR, 
                         text="HOST:", font=FONT_BOLD, padx=1, pady=10)
        ip_label.place(relwidth=0.2, rely=0.15)
        
        
        ip_label_fianco = Label(self.login_window, height= 3, bg=BG_COLOR)
        ip_label_fianco.place(relwidth=0.7, relx=0.25, rely=0.137)
        
        #label PORT
        port_label = Label(self.login_window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="PORT:", font=FONT_BOLD, padx=1, pady=10)
        port_label.place(relwidth=0.2, rely=0.35)
        
        port_label_fianco = Label(self.login_window, height= 3, bg=BG_COLOR)
        port_label_fianco.place(relwidth=0.7, relx=0.25, rely=0.34)
        
        #label nickname
        nick_label = Label(self.login_window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Nickname:", font=FONT_BOLD, padx=1, pady=10)
        nick_label.place(relwidth=0.2, rely=0.6)
        
        nick_label_fianco = Label(self.login_window, height= 3, bg=BG_COLOR)
        nick_label_fianco.place(relwidth=0.7, relx=0.25, rely=0.585)
        
        #label pulsante login credenziale
        pulsante_login_label = Label(self.login_window, height=3, bg=LOGIN_BG)
        pulsante_login_label.place(relwidth=1, rely=0.825)
        
        #pulsante login
        pulsante_login = Button(pulsante_login_label, text="Login", font=FONT_BUTTON, width=5, bg=BUTTON_COLOR, 
                                command=lambda: self._premere_enter_log(None))
        pulsante_login.place(relx=0.39, relheight=1, relwidth=0.22)
        
        def _premere_enter_log(self, event):
            self.host_entry.get()
            self.port_entry.get()
            self.nick_entry.get()
        
        def _data_entry_verify():
            global INSERTED_HOST
            global INSERTED_PORT
            INSERTED_HOST = self.host_entry.get()
            INSERTED_PORT = self.port_entry.get()
            
            if INSERTED_HOST is HOST and INSERTED_PORT is PORT:
                    _login_success()
                    
                           
        def _login_success():
            self.login_window.withdraw()
            self.window.deiconify()
            
        
        #box inserimento testo HOST
        self.host_entry = Entry(ip_label_fianco, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.host_entry.place(relwidth=1, relheight=1, rely=0.008, relx=0.011)
        self.host_entry.focus()
        
        
         #box inserimento testo PORT
        self.port_entry = Entry(port_label_fianco, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.port_entry.place(relwidth=1, relheight=1, rely=0.008, relx=0.011)
        self.port_entry.focus()
     
        #box inserimento testo NICK
        self.nick_entry = Entry(nick_label_fianco, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.nick_entry.place(relwidth=1, relheight=1, rely=0.008, relx=0.011)
        self.nick_entry.focus()
    
  
    
  
class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat Game")
        self.window.resizable(width=False, height=False)
        self.window.configure(width= 500, height= 550, bg=BG_COLOR)
        
        
        
        #head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                            text="Benvenuto!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        #divisore
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        #widget di testo
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.645, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        #barra di scorrimento
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        #label in basso
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        #label per i tasti a, b e c
        under_label = Label(self.window, height=4, bg=BG_GRAY)
        under_label.place(relwidth=1, rely=0.723)
        
        
        #box inserimento testo
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._premere_enter)
        
        # pulsante invio messaggio
        pulsante_invio = Button(bottom_label, text="Invia", font=FONT_BOLD, width=20, bg=BG_GRAY,
                                command=lambda: self._premere_enter(None))
        pulsante_invio.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        #pulsante a
        pulsante_a = Button(under_label, text="a", font=FONT_BUTTON, width=5, bg=BUTTON_COLOR,
                            command=lambda: self._premere_Char("a"))
        pulsante_a.place(relx=0.1, rely=0.2, relheight=0.7, relwidth=0.22)
        
        
        #pulsante b
        pulsante_b = Button(under_label, text="b", font=FONT_BUTTON, width=5, bg=BUTTON_COLOR,
                            command=lambda: self._premere_Char("b"))
        pulsante_b.place(relx=0.39, rely=0.2, relheight=0.7, relwidth=0.22)
        
        
        #pulsante c
        pulsante_c = Button(under_label, text="c", font=FONT_BUTTON, width=5, bg=BUTTON_COLOR,
                            command=lambda: self._premere_Char("c"))
        pulsante_c.place(relx=0.68, rely=0.2, relheight=0.7, relwidth=0.22)
        
    def _premere_Char(self, char):
        self._inserisci_messaggio(char, "Tu")
        
    
    def _premere_enter(self, event):
        msg = self.msg_entry.get()
        self._inserisci_messaggio(msg, "Tu")
        
    def _inserisci_messaggio(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
   
    

    
   
    
if __name__ == "__main__":
    app = LoginApplication()
    app = ChatApplication()
    print(app.text_widget)
    app.run()
    