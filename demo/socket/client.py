import socket

port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    server.sendto(b"Hello udp! It's work.", ('localhost', port))

