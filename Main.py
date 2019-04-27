from _thread import *
import sys
import socket
import ShortGame
import PlayerData

Short = []
Med = []
Long = []

def LoadPlayerID(rawData):
    PlayerID = ""
    for i in range(len(rawData)):
        if rawData[i] == ":":
            PlayerID = rawData[i+1:]
            start_new_thread(PlayerData.readyPlayer, (PlayerID,))
            break

def Queue():
    global Short, Med, Long
    while True:
        if len(Short) == 4:
            start_new_thread(ShortGame.Main, (smallPort,))
            for i in Short:
                try:
                    Med.remove(i)
                except:
                    pass
                try:
                    Long.remove(i)
                except:
                    pass
                i[0].send("Short\n".encode())
                i[0].close()
            Short = []
        elif len(Med) == 4:
            #start_new_thread(ShortGame.Main, (smallPort,))
            for i in Med:
                try:
                    Short.remove(i)
                except:
                    pass
                try:
                    Long.remove(i)
                except:
                    pass
                i[0].send("Medium\n".encode())
                i[0].close()
        elif len(Long) == 8:
            #start_new_thread(ShortGame.Main, (smallPort,))
            for i in Long:
                try:
                    Med.remove(i)
                except:
                    pass
                try:
                    Short.remove(i)
                except:
                    pass
                i[0].send("Long\n".encode())
                i[0].close()

def main(conn, addr):
    while True:
        try:
            data = conn.recv(4096)
        except:
            conn.close()
            data=False
        if not data:
            print("Main. Disconnected from " + addr[0] + ":" + str(addr[1]))
            try:
                Short.remove([conn,addr])
            except:
                pass
            try:
                Med.remove([conn,addr])
            except:
                pass
            try:
                Long.remove([conn,addr])
            except:
                pass
            break
        data = data.decode()[2:]
        print ("Main. "+data)
        if "Queue" in data:
            if "Queue1" in data:
                Short.append([conn,addr])
            if "Queue2" in data:
                Med.append([conn,addr])
            if "Queue3" in data:
                Long.append([conn,addr])
        elif "Echo" in data:
            conn.send("Affirm\n".encode())
            conn.close()
            print("Main. Disconnected from " + addr[0] + ":" + str(addr[1]))
            LoadPlayerID(data)
            break
        elif "Stats" in data:
            conn.send((PlayerData.GetStats(data) + "\n").encode())
            conn.close()
            print("Main. Disconnected from " + addr[0] + ":" + str(addr[1]))



start_new_thread(Queue,())

host = ""
try:
    port = int(input("Ports are one after each other so there must be 4 free ports, starting from entered port.\nPut in the main port: "))
    smallPort = port+1
    medPort = port+2
    largePort = port+3
except:
    print("Port Error")
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

while True:
    conn, addr = sock.accept()
    print("Main. Connected with " + addr[0] + ":" + str(addr[1]))
    start_new_thread(main, (conn,addr,))
    
    
sock.close()
sys.exit()
    
    

    
    
    
    
    
    
    
    
    
    
    
    