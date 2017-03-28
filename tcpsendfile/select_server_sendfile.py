import socket
import sys
import select

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(10)

list_conn = [sock]
print "Starting server"
print >>sys.stderr, 'waiting for a connection'
try :
    while True :
        input_ready, output_ready, error_ready = select.select(list_conn, [], [])
        for i in input_ready :
            if i == sock :
                conn, addr = sock.accept()
                list_conn.append(conn)
            else :
                try :
                    fileout = 'recieved/'+i.recv(256)
                    print 'write to ' + fileout
                    i.sendall("Request have been processed")
                    print 'processing'
                    fileoutput = open(fileout, 'w')
                    try :
                        while True :
                            line = i.recv(256)
                            fileoutput.write(line)
                            if line == '':
                                fileoutput.close()
                                break
                        list_conn.remove(i)
                        i.close()
                        print "client disconnected"
                    except socket.error :
                        list_conn.remove(i)
                        i.close()
                        print "client disconnected"
                except socket.error :
                    list_conn.remove(i)
                    i.close()
                    print "client error"
except KeyboardInterrupt :
    print "I have dieded"
