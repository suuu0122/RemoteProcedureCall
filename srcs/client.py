import json
import socket
import sys

class Client:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def start(self):
        try:
            self.sock.connect(self.server_address)
        except socket.error as err:
            print(err)
            sys.exit(1)

        while True:
            try:
                message = open("../json/sample1.json", 'r')
                message_dict = json.load(message)
                message_json = json.dumps(message_dict)
                self.sock.sendall(message_json.encode("utf-8"))
                message.close()

                response = self.sock.recv(4096).decode("utf-8")
                if response:
                    print(f"Server response: {response}")
                else:
                    break
            finally:
                print("\nClosing socket")
                self.sock.close()
                sys.exit()
                break

if __name__ == '__main__':
    client = Client("socket_file")
    client.start()
