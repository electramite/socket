import socket
clientsocket = socket.socket()
host = "134.209.146.121"
port = 4582



try:
	clientsocket.connect((host, port))
	print("connection established...")
except socket.error as e:
	print(str(e))
while True:
	inp = input("angle.....?")
	clientsocket.send(str.encode(inp))
clientsocket.close()