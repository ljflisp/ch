import socket
import time
time.sleep(1)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.bind((socket.gethostname(),5081))
client.connect((socket.gethostname(),5099))

a = input()
client.send(bytes(a.encode("ascii")))
	
	
if a == "exit":
	quit()

client.close()
import os
os.system("python Client.py")

