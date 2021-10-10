import datetime
import pytz
def time_():
	return datetime.datetime.now(pytz.timezone('GMT')).strftime("%a, %d %b %Y %X %Z")
print(time_())
def response_message(status,data=0):
        return '''HTTP/1.1 %s
Connection: close
Date: %s
Server: Apache/2.2.3 (CentOS)
Last-Modified: %s
Content-Length: %d
Content-Type: text/html

%s''' %(status,time_(),time_(),data,'None')
print(response_message('404 Not found'))
