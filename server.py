import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(1)
conn, address = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()

