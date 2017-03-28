import socket
import sys
from thread import start_new_thread

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(10)

def handle_connection(conn) :
    fileout = 'recieved/'+connection.recv(256)
    print 'write to ' + fileout
    connection.sendall("Request have been processed")
    print 'processing'
    fileoutput = open(fileout, 'w')
    try :
        while True :
            line = connection.recv(256)
            fileoutput.write(line)
            if line == '':
                fileoutput.close()
                break
        connection.close()
        print "client disconnected"
    except socket.error :
        connection.close()
        print "client disconnected"

try :
    while True :
        print "Starting server"
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        start_new_thread(handle_connection, (connection,))
except KeyboardInterrupt :
    print "I have dieded"
