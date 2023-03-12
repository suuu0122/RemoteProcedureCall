require "json"
require "socket"

server_address = "socket_file"
sock = UNIXSocket.new(server_address)

json_file = File.open("../json/sample1.json", 'r')
message_hash = JSON.load(json_file)
json_file.close

message_json = JSON.dump(message_hash)

sock.send(message_json, 0)


