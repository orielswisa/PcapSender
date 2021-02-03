import socket


skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

port = input("Enter port number: ")
skt.bind(('',int(port)))
while True:
    c, addr = skt.recvfrom(1024)
    print("got connection",addr)
    print(c)