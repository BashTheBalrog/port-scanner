import socket
#Importing the socket package
#This program is written to scan a hostname for open ports and ping them
print("Hello User to BashTheBalrog's Port Scanner")
target=input("Enter IP address or hostname: ")
print(target)
ip=socket.gethostbyname(target)
print("IP: ")
print(ip)
print("Scan one port => 1 OR Scan ALL PORTS => 2")
choice=int(input("Enter your choice: "))
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(1)
print(sock)
if choice==1:
    port=int(input("Enter port number to scan: "))
    result=sock.connect_ex((ip,port))
    print(result)

    if result==0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
elif choice==2:
    for port in range(1,65535):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.05)
        result=sock.connect_ex((ip,port))
        if result==0:
            print(f"Port {port} is OPEN")
        #else:
           # print(f"Port {port} is CLOSED")
sock.close()