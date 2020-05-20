import socket
import sys
import itertools

lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all = lower_a + num

def get_comb():
    for r in range(2, 4):
        for s in itertools.product(all, repeat=r):
             yield ''.join(s)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('52.49.91.111', 2003)
sock.connect(server_address)

received = sock.recv(1000)
if received:
    data = received.decode()
    print(data)

sock.sendall("a".encode())
received = sock.recv(1000)
wrong_data = received.decode()

try:
    print("Trying")
    for cmd in get_comb():
        print(cmd)
        # Send data
        #message = input("")
        sock.sendall(cmd.encode())

        received = sock.recv(1000)
        if received and received.decode() != wrong_data:
            print(received.decode())

finally:
    sock.close()
