import socket
import struct
import time
def get_msg():
    udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("",13117))
    #self.udp_socket.settimeout(0.5)
    print("hi1")
    message=""
    while message=="":
        try:
            udp_socket.settimeout(0.5)  
            message=udp_socket.recvfrom(1024)
            print("hi")
            print(message.decode())
        except:
            continue
    return message

def start():
    #starting the client
    print("Client started, listening for offer requests...")
    while 1: #wait for offers
        msg,addr=get_msg() #get msg and adress
        print(msg)
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
    ip,_=addr
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        tcp_socket.connect((ip,port))
        tcp_socket.send(bytes("temp\n",'utf-8'))
        msg=tcp_socket.recv(1024).decode('utf-8')
    except:
        print("eror")
    print(msg) #welcome msg
    start_game(tcp_socket) #move to the game
    

def start_game(tcp_socket):
    #start=time.time()
    try:
        msg=tcp_socket.recv(1024).decode('utf-8')
        print(msg)
        answer=input()
        tcp_socket.send(bytes(answer+'\n','utf-8'))    
    except:
        return

    


    

start()