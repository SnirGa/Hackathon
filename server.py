import socket
import threading
import concurrent
import time
import struct
from termcolor import colored

class server:
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.devlop_net = "172.1.255.255"
        self.port=2131
        self.broadcast_post=13117
        self.buffersize=1024
        self.host_name=socket.gethostname()
        self.host_ip=socket.gethostbyname(self.host_name)
        self.teams=[]

    def start_broadcast(self):
        threading.Timer(1,self.start_broadcast).start()
        msg=struct.pack(0xabcddcba,0x2,self.port)
        self.udp_socket.sendto(msg,(self.devlop_net,self.broadcast_post))
    
    def waiting_for_clients(self):
        threading.Thread(target=self.start_broadcast).start()
        while len(self.teams)<=2:
            self.tcp_socket.settimeout(0.1)
            try:
                client,address=self.tcp_socket.accept()
                group_name=client.recv(self.buffersize).decode("utf-8")
                time.sleep(0.1)
                tup=(client,address,group_name)
                self.teams.append(tup)
                print(colored(f'{group_name} entered the game!','blue'))
            except:
                print(colored("there is no space left","red"))
                continue
        
    
    
    def start_game(self,client):
        start_time=time.time()
        while time.time()-start_time<=10:
            try:
                client.settimeout(0.01)
                answer=client.recv(self.buffersize).decode("utf-8")
                answer_time=time.time()
            except:
                pass
        
        return answer,answer_time

         



