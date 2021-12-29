import socket
import struct
import time
import sys
def get_msg():
    print("client:get_msg method")
    udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("",13117))
    #self.udp_socket.settimeout(0.5)
    message=""
    while message=="":
        print('loop')

        try:
            udp_socket.settimeout(0.5)  
            message=udp_socket.recvfrom(1024)
        except:
            continue
    return message

def start():
    print("client:start method")

    #starting the client
    print("Client started, listening for offer requests...")
    while 1: #wait for offers
        msg,addr=get_msg() #get msg and adress
        try: #verify what message recieved, if not good- continue
            msg2=struct.unpack("Ibh",msg)
            if msg2[0] != 4276993775 or msg2[1] != 2 or msg2[2] < 1024 or msg2[2] > 32768:
                continue
        except:
            continue
        port=msg2[2]
        try: #attempting to connect tcp
            tcp_connection(addr,port)
        except:
            continue
        print("Server disconnected, listening for offer requests...")



def tcp_connection(addr,port):
    print("client:tcp_connection method")

    ip,_=addr
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        tcp_socket.connect((ip,port)) #socket connect to the server
        tcp_socket.send(bytes("temp\n",'utf-8')) 
    except ValueError:
        print("error")
    start_game(tcp_socket) #move to the game
    
    

def start_game(tcp_socket):
    print("client:start_game method")


    #start=time.time()
    try:
        msg=tcp_socket.recv(1024).decode('utf-8') 
        print(msg) #welcome msg

        msg=tcp_socket.recv(1024).decode('utf-8')
        print(msg) #get question
        answer=sys.stdin.readline()[0]
        tcp_socket.send(bytes(answer+'\n','utf-8'))    
    except:
        return

start()