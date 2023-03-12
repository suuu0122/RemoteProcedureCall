import json
import os
import socket
import sys
import threading

class Server:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    def connect(self):
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        self.sock.bind(self.server_address)
        self.sock.listen(5)
        print("Server listening")
    
    def start(self):
        sock = self.sock
        self.connect()
        
        while True:
            try:
                conn, addr = sock.accept()
            except KeyboardInterrupt:
                print("\nClosing socket")
                os.unlink(self.server_address)
                sock.close()
                sys.exit()
                break
            res = conn.recv(4096)
            print(res.decode("utf-8"))

if __name__ == '__main__':
    server = Server("socket_file")
    server.start()
