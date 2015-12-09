#!/usr/bin/env python
import sys
import socket
import json
TCP_IP = '192.168.1.61'
TCP_PORT = 2081
BUFFER_SIZE = 10
MESSAGE = "7"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
return_code = unicode(data)
success=0
message=""

if return_code =="\x03\x00~":
	success=1
	message="brewing"
elif return_code=="\x03\x01~":
	message="already brewing"
elif return_code=="\x03\x05~":
	message="no carafe"
elif return_code=="\x03\x06~":
	message="no water"
else:
	message="check machine"

print json.dumps({'success': success,'message':message,'return_code':repr(data)[1:10]})

quit()
sys.exit()
