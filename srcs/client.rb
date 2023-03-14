require "json"
require "socket"

class Client
	def initialize(server_address)
		@server_address = server_address
	end

	def start
		sock = UNIXSocket.new(@server_address)

		json_file = File.open("../json/sample2.json", 'r')
		message_hash = JSON.load(json_file)
		json_file.close
		
		message_json = JSON.dump(message_hash)
		sock.send(message_json, 0)
		
		puts "Server response: " + sock.recv(4096)
		sock.close
		puts "Closing socket"
	end
end

client = Client.new("socket_file")
client.start
