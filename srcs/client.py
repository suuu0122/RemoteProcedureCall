import json
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "socket_file"

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

while True:
    try:
        message = open("../json/sample1.json", 'r')
        message_dict = json.load(message)
        message_json = json.dumps(message_dict)
        sock.sendall(message_json.encode("utf-8"))
    except KeyboardInterrupt:
        print("\nClosing socket")
        sock.close()
        sys.exit()
        break