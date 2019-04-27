import socket
import sys
from _thread import *

host = ""
port = 888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("Socket Created")

try:
    s.bind((host, port))
except socket.error:
    print("Binding Failed")
    sys.exit()
    
print("Sock has been bound")

s.listen(10)

print("Socket is Ready")

def clientthread(conn):
    conn.send("Welcome to the Server. Type something and hit enter\n".encode())
    
    while True:
        data = conn.recv(1024)
        reply = ("OK. " + data.decode()).encode()
        if not data:
            break
        conn.sendall(reply)
    print (reply.decode())
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    start_new_thread(clientthread, (conn,))


s.close()
c.close()