#! /usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.200', 9999))

s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))




