import socket
import sys
PORT = 8080
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREA>
print('sicket has been create')
try:
 mysocket.bind("", 8080)
except socket.error as msg:
 print('Binding failed in code :' +str(msg[0] + 'Message' >
import sys
sys.exit()
 print('socket binding is now complete')
mysSocket.listen(10)
 print('socket is now in listening mode')
while 1:
connection, address = mySocket.accept()
 print('connection with' + address[0] + ':' str(address[1]>
mySocket.close()