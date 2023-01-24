import threading
import tkinter
from tkinter import *
from tkinter import messagebox
from RubixCuberLogin import Login
from RCGameMenu import GameMenu
from UserDb import User
import  socket
from tkinter import ttk


class FMenu(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.title('Main Window')
        self.handle_thread_socket()

        self.lbl_email = Label(self, width=10, text="email :")
        self.lbl_email.place(x=10, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=100, y=50)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=10, y=100)
        self.password = Entry(self, width=20)
        self.password.place(x=100, y=100)

        self.lbl_name = Label(self, width=10, text="name :")
        self.lbl_name.place(x=10, y=150)
        self.name = Entry(self, width=20)
        self.name.place(x=100, y=150)

        self.buttonReg = Button(self, text="register", command=self.register_user, width=20, background="blue")
        self.buttonReg.place(x=10, y=200)

        self.buttonLog = Button(self, text="Login", command=self.open_login, width=20, background="red")
        self.buttonLog.place(x=10, y=230)

        self.buttonG = Button(self, text="game", command=self.open_game, width=20, background="red")
        self.buttonG.place(x=10,y=250)



    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1802))
        data = self.client_socket.recv(1024).decode()
        print(data)

    def register_user(self):
        name = self.name.get()
        password = self.password.get()
        email = self.email.get()
        time = "yes"
        self.client_socket.send(("register" + "," + email + "," + password + "," + name + "," + time).encode())
        GameWindow = GameMenu(self)

    def open_login(self):
        window = Login(self)
        window.grab_set()
        self.withdraw()

    def open_game(self):
        GameWindow = GameMenu(self)
        GameWindow.grab_set()
        self.withdraw()

if __name__ == "__main__":
    menu = FMenu()
    menu.mainloop()