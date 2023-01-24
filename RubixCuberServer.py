import multiprocessing
import socket
import threading
from UserDb import User


cores = multiprocessing.cpu_count()
print(cores)

class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running=True
       self.UserDb = User()

   def start(self):
       try:
           print('server starting up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.sock.bind((self.ip, self.port))
           self.sock.listen(3)

           while True:
               print('waiting for a new client')
               clientSocket, client_addresses = self.sock.accept()
               print('new client entered')
               clientSocket.send('Hello this is server'.encode())
               self.count += 1
               print(self.count)
               # implement here your main logic
               self.handleClient(clientSocket, self.count)

       except socket.error as e:
           print(e)

   def handleClient(self, clientSock, current):
       client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
       client_handler.start()

   def handle_client_connection(self, client_socket, current):
       not_crash = True
       print(not_crash)
       while self.running:
                   server_data = client_socket.recv(1024).decode('utf-8')
                   #insert,email,password,firstname
                   arr = server_data.split(",")
                   server_data = arr
                   print(arr)
                   if arr!=None and arr[0]=="register" and len(arr)==5:
                       print("register user")
                       print(arr)
                       server_data=self.UserDb.insert_user(arr[1], arr[2], arr[3], arr[4])
                       print("server data:",server_data)
                       if server_data:
                           client_socket.send("success register".encode())
                       elif server_data:
                           client_socket.send("failed register".encode())

                   elif arr!=None and arr[0] == "login" and len(arr)==3:
                       print("login user")

                       server_data=self.UserDb.return_login(arr[1],arr[2])
                       if server_data == True:
                           client_socket.send("succes login".encode())
                       else:
                           client_socket.send("False".encode())
                   else:
                       server_data="False"
                       self.running == False



if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 1802
   s = Server(ip, port)
   s.start()