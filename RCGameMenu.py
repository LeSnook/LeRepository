import tkinter
import threading
from tkinter import *
from UserDb import User
import  socket
from CubeImplement import Cube


class GameMenu(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x400')
        self.handle_thread_socket()
        self.title('Toplevel Window 3')

        self.ButtonClose = Button(self, text='X', command=self.close, width=2, background="red")
        self.ButtonClose.place(x=380, y=0)

        self.welc = Label(self, width=10, text="Welcome" )
        self.welc.place(x=200,y=100)

        self.ButtonTut = Button(self, text='Tutorial', command=self.open_tutorial, width=10, background="blue")
        self.ButtonTut.place(x=200, y=200)

        self.ButtonFree = Button(self, text='Free Mode', command=self.open_free, width=10, background="blue")
        self.ButtonFree.place(x=200, y=250)

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1802))
        data = self.client_socket.recv(1024).decode()
        print(data)

    def open_tutorial(self):
        print("tutorial")

    def open_free(self):
        new_window = Toplevel(self)
        new_window.geometry('400x400')
        new_window.title("Free Mode")
        new_window.mainloop()
        butr = Button(self,text="R", command=Cube._key_press("right"))
        butr.place(x=100,y=100)

    def close(self):
        self.parent.deiconify()
        self.destroy()
