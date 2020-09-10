# myServer.py will create a Kali Web Server
print('Wait for connection..................')
print('It take a while...................')
print('This code is created Sumbal khan Certified Ethical Hacker..........')
print('Note: It should be noted that Iam not responsibles for any illegals activities.')
print('use for eduction purposes only')
print('Follow and support me for more Tools.')
print('Facebook: www.facebook.com/Sumbalstricks.termux.12')
import socket
import sys


74
# We need to pass an empty string, so that all interfaces are available

# You can choose any arbitrary port number
PORT = 8080
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket has been created')
# Let us bind the socket to local host and port
try:
 mysocket.bind(("", PORT))
except socket.error as msg:
 print('Binding has failed. Error Code is : ' + str(msg[0])
+ ' Message ' + msg[1])
sys.exit()
print('Socket bind is complete. Now we can proceed to make it listen...')
# Server is listening now on socket
mySocket.listen(10)
print('Socket is now listening')
# Let the server keep talking with the client
while 1:
# We are waiting to accept a connection - blocking call
 connection, address = mySocket.accept()

print('Connected with ' + address[0] + ':' + str(address[1]))
connection.send('Successfully create connection. Thank You for Connection')
mySocket.close()
