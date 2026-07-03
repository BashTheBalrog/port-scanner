import socket
import time
from concurrent.futures import ThreadPoolExecutor
#Importing the socket package

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    resu = sock.connect_ex((ip, port))
    sock.close()
    return resu

#This program is written to scan a hostname for open ports and ping them
print("="*50)
print("          PYTHON TCP PORT SCANNER")
print("="*50)
print("Hello User to BashTheBalrog's Port Scanner")
target=input("Enter IP address or hostname: ")
print(target)
try:
    ip=socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    exit()
print("IP: ")
print(ip)
print("Scan one port => 1 OR Scan ALL PORTS => 2 OR Scan a range of ports => 3")
choice=int(input("Enter your choice: "))
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(1)
start_time=time.time()
print(sock)
if choice==1:
    port=int(input("Enter port number to scan: "))
    result=scan_port(ip, port)
    print(result)

    if result==0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
elif choice==2:
    open_ports=0
    for port in range(1,65535):
        result=scan_port(ip, port)
        if result==0:
            print(f"Port {port} is OPEN")
            open_ports += 1
    print(f"Total open ports found: {open_ports}")
    #else:
           # print(f"Port {port} is CLOSED")
elif choice==3:
    sp=int(input("Enter starting port number to scan: "))
    ep=int(input("Enter ending port number to scan: "))
    open_ports=0
    for port in range(sp, ep+1):
        result=scan_port(ip, port)
        if result==0:
            print(f"Port {port} is OPEN")
            open_ports += 1
    print(f"Total open ports found: {open_ports}")
    #else:
           # print(f"Port {port} is CLOSED")
sock.close()
end_time=time.time()
print(f"Scan completed in {end_time - start_time} seconds")