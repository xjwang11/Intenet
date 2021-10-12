from socket import *
Serversocket=socket(AF_INET,SOCK_DGRAM)
Port=12000
Serversocket.bind(('',Port))
print('The server is ready to receive')
while True:
	message,clientAddress=Serversocket.recvfrom(2048)
	Serversocket.sendto(message,clientAddress)
