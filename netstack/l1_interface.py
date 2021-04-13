import socket

ETH_P_ALL = 3
MAX_PKT_SIZE = 4096


class Interface:
    name = None
    rawSocket = None

    def __init__(self, interface_name):
        print("Initializing interface...")
        self.name = interface_name
        self.rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
        self.rawSocket.bind((self.name, 0))

    def receive(self):
        return self.rawSocket.recv(MAX_PKT_SIZE)

    def send(self, data):
        return self.rawSocket.send(data)

    def __del__(self):
        print("Deinitializing ethernet...")
        self.rawSocket.close()
