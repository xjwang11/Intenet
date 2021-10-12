from socket import *
import time
from func_timeout import func_set_timeout
import eventlet
Host='192.168.0.105'
Port=12000
time_limit=1.0#
Clientsocket=socket(AF_INET,SOCK_DGRAM)#create a socket and uses IPV4 and UDP protocol.
@func_set_timeout(1)
def task(socket):
	return socket.recvfrom(1024)
for i in range(1,11):
	Clientsocket.sendto('test'.encode(),(Host,Port))
	begin_time=time.time()
	Flag=1
	
	try:
		message,serverAddress=task(Clientsocket)
	
		end_time=time.time()
	
	except:
		print('The %d one failed'%i)
		Flag=0
	if Flag==1:
		print('It takes %d ' %(end_time-begin_time))
	

	
