import tkinter
import threading
from tkinter import *
from tkinter import messagebox
from UserDb import User
from RCGameMenu import GameMenu
import  socket
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x400')
        self.handle_thread_socket()
        self.title('Login')

        self.lbl_email = Label(self, width=10, text="email :")
        self.lbl_email.place(x=10, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=100, y=50)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=10, y=100)
        self.password = Entry(self, width=20,show="*")
        self.password.place(x=100, y=100)


        self.ButtonClose = Button(self, text='X', command=self.close, width=2, background="red")
        self.ButtonClose.place(x=380,y=0)

        self.ButtonLog = Button(self, text='Login', command = self.Login_User, width = 10, background="yellow")
        self.ButtonLog.place(x=100,y=150)

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1802))
        data = self.client_socket.recv(1024).decode()
        print(data)

    def Login_User(self):
        password = self.password.get()
        email = self.email.get()
        self.client_socket.send(("login" + "," + email + "," + password).encode())
        data = self.client_socket.recv(1024).decode()
        print(data)
        if data == "succes login":
            GameWindow = GameMenu(self)
        elif data == "False":
            messagebox.showerror('error',"invalid pass")
    def close(self):
        self.parent.deiconify()
        self.destroy()