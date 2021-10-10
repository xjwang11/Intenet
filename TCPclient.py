from socket import *
def get_url(url,host,port):
	return '''GET %s HTTP/1.1
Host: %s
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr
''' %(url,host)
host='192.168.0.102'
port=12000
clientsocket=socket(AF_INET,SOCK_STREAM)
clientsocket.connect((host,port))
clientsocket.send(get_url('/Users/aizanghuaren/Desktop/python/variable_test.py',host,port).encode())
message=clientsocket.recv(1024).decode()
print(message)
clientsocket.close()
