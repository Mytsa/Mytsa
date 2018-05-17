# import socket
# import json
#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind the socket to the port
# server_address = ('localhost', 9999)
# print('starting up on {} port {}'.format(*server_address))
# sock.bind(server_address)
#
# # Listen for incoming connections is 5 client
# sock.listen(5)
#
# while True:
#     # Wait for a connection
#     print('waiting for a connection')
#     connection, client_address = sock.accept()
#     try:
#         print('connection from', client_address)
#
#         # Receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(16)
#             print('received {!r}'.format(data))
#             if data:
#                 print('sending data back to the client')
#                 connection.sendall(data)
#             else:
#                 print('no data from', client_address)
#                 break
#
#     finally:
#         # Clean up the connection
#         connection.close()
#

import socket
from threading import *
from time import sleep
from datetime import datetime


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 9999))

class client(Thread):
    def __init__(self, socket, address, tst):
        Thread.__init__(self)
        self.sock = socket
        self.adrs = address
        self.tst = tst
        self.start()


    def run(self):
        while 1:
            print('Client from server sent:', self.sock.recv(1024).decode())
            a = str(self.tst)
            self.sock.send(a.encode())


serversocket.listen(5)
print('server started and listening')
while 1:
    for i in range(0, 10):
        tst = datetime.timestamp(datetime.now())
        clientsocket, address = serversocket.accept()
        client(clientsocket, address, tst)
        print(i)
        sleep(1)
        i += i
    # sleep(10)
    # print("finish server")
    # serversocket.close()




