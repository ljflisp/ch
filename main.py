import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((socket.gethostname(),5099))
server.listen()
while True:
	c,a = server.accept()
	clients = [].append(c)
	
	try:
		
		print(c.recv(1024).decode("utf-8"))
	except:
		for x in clients:
			print(x.recv(1024).decode("utf-8"))
			
	