from socket import *
ServerPort=12000
ServerSocket=socket(AF_INET,SOCK_STREAM)
ServerSocket.bind(('',ServerPort))
ServerSocket.listen(1)
while True:
	connectionSocket,address=ServerSocket.accept()
	message=connectionSocket.recv(2014).decode()
	path=message.split()[1]
	print(path)
	connectionSocket.close()
	
