import socket
import sys
import itertools


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('52.49.91.111', 9876)
sock.connect(server_address)

sock.sendall("GET /games/cat_fight/get_key HTTP/1.1\nHost:pre.steam-origin.contest.tuenti.net\n\n".encode())
received = sock.recv(1000)
print(received.decode())
