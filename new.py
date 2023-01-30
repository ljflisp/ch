import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.bind((socket.gethostname(),5087))
client.connect((socket.gethostname(),5099))


a = input()
client.send(bytes(a.encode("utf-8")))

client.close()