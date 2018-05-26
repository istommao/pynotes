import socket

port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #udp

server.bind(('', port))

print('Listen on port: %s' % port)

while True:
    data, addr = server.recvfrom(1024)
    print('Received from %s data: %s' % (addr, data))

