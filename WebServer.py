from socket import *
import os
import datetime
import pytz
def time_():
        return datetime.datetime.now(pytz.timezone('GMT')).strftime("%a, %d %b %Y %X %Z")
print(time_())
def response_message(status,data=''):
        return '''HTTP/1.1 %s
Connection: close
Date: %s
Server: Apache/2.2.3 (CentOS)
Last-Modified: %s
Content-Length: %d
Content-Type: text/html

%s''' %(status,time_(),time_(),len(data),data)

ServerPort=12000
ServerSocket=socket(AF_INET,SOCK_STREAM)
ServerSocket.bind(('',ServerPort))
ServerSocket.listen(1)
while True:
	connectionSocket,address=ServerSocket.accept()
	message=connectionSocket.recv(2014).decode()
	path=message.split()[1]
	if os.path.exists(path):
		print('the file exists!')
		file=open(path)
		try:
			text=file.read()
		finally:
			file.close()
		connectionSocket.send(response_message('200 OK',text).encode())
	else:
		print("the file doesn't exist")
		connectionSocket.send(response_message('404 Not found').encode())
	connectionSocket.close()
	
