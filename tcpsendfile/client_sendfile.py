import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)

print 'connecting to %s port %s' % server_address
sock.connect(server_address)
# Send data
filein = raw_input('Enter file name : ')
sock.sendall(filein)
# Look for the response
print sock.recv(256)
files = open(filein, 'r')
with files as fileinput :
    for line in fileinput :
        sock.sendall(line)
print 'closing socket'
sock.close()
