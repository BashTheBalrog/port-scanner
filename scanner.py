import socket
#Importing the socket package
#This program is written to scan a hostname for open ports and ping them
print("Hello User to BashTheBalrog's Port Scanner")
target=input("Enter IP address or hostname: ")
print(target)
ip=socket.gethostbyname(target)
print("IP: ")
print(ip)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(sock)