import socket
import threading
import struct
import time
class server:
    def __init__(self):
        self.port=2031
        self.IP=socket.gethostbyname(socket.gethostname())
        self.format='utf-8'
        self.tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #self.udp_socket.bind('localhost',13117) #check!!!
        self.teams=[]
        self.udp_port=13117
        self.buffer=1024
        self.develop_net = socket.gethostbyname(socket.gethostname())#"172.1.255.255"

    
    def start_broadcast(self):
        threading.Timer(1.0,self.start_broadcast).start()
        msg = struct.pack("Ibh",0xabcddcba,0x2,self.port)
        self.udp_socket.sendto(msg,(self.develop_net,self.udp_port))
        
        #msg="hello world".encode()
        #addr=(self.develop_net,self.udp_port)
        #self.udp_socket.sendto(msg,addr)

    def wait_for_clients(self):
        thread=threading.Thread(target=self.start_broadcast)
        thread.start()
        while len(self.teams)<2:
            self.tcp_socket.settimeout(0.1)
            try:
                client,address=self.tcp_socket.accept()
                group_name=client.recv(self.buffersize).decode("utf-8")
                #time.sleep(0.1)
                tup=(client,address,group_name)
                self.teams.append(tup)
                print(f'{group_name} entered the game!')
            except:
                continue
    
    def game(self,client):
        self.tcp_socket.listen()




        


    def start(self):
        print(f"Server started, listening on IP address {self.IP}")
        self.wait_for_clients()

        


class team:
    def __init__(self,name,IP,port):
        self.name
        self.team_ip=IP
        self.team_port=port


s=server()
s.start()