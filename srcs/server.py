import json
import math
import os
import socket
import sys
import threading

class Process:
    @classmethod
    def process_method(cls, method, params):
        if (method == "floor"):
            return Process.method_floor(params)
        elif (method == "nroot"):
            return Process.method_nroot(params)
        elif (method == "reverse"):
            return Process.method_revrese(params)
        elif (method == "validAnagram"):
            return Process.method_validAnagram(params)
        elif (method == "sort"):
            return Process.method_sort(params)
        else:
            return "Error"
        
    @staticmethod
    def method_floor(params):
        return math.floor(params[0])
    
    @staticmethod
    def method_nroot(params):
        n = params[0]
        x = params[1]
        return math.pow(x, 1/n)
    
    @staticmethod
    def method_revrese(params):
        str = params[0]
        return str[::-1]
    
    @staticmethod
    def method_validAnagram(params):
        str1 = params[0]
        str2 = params[1]
        if str1 is None or str2 is None or len(str1) != len(str2):
            return False
        return True if sorted(str1) == sorted(str2) else False
    
    @staticmethod
    def method_sort(params):
        sorted_arr = sorted(params)
        return sorted_arr
        

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
    
    def recv_handler(self, conn, addr):
        recv_message = conn.recv(4096)
        recv_message_json_str = recv_message.decode("utf-8")
        recv_message_dict = json.loads(recv_message_json_str)
        print(f"Recieve: {recv_message_dict}")
            
        method = recv_message_dict["method"]
        params = recv_message_dict["params"]
        id = recv_message_dict["id"]
            
        result = Process.process_method(method, params)
        response_dict = {}
        response_dict["result"] = result
        response_dict["result_type"] = type(result).__name__
        response_dict["id"] = id
            
        response_json = json.dumps(response_dict)
        conn.sendall(response_json.encode("utf-8"))
    
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

            thread = threading.Thread(target=self.recv_handler, args=(conn, addr))
            thread.start()

if __name__ == '__main__':
    server = Server("socket_file")
    server.start()
