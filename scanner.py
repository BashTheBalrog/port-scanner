import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# Function to scan a single port
def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex((ip, port))


# Banner
print("=" * 50)
print("          PYTHON TCP PORT SCANNER")
print("=" * 50)
print("Hello User to BashTheBalrog's Port Scanner")

# Get target
target = input("Enter IP address or hostname: ")

try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting.")
    exit()

print(f"\nResolved IP: {ip}")

print("\nChoose an option:")
print("1. Scan one port")
print("2. Scan ALL ports")
print("3. Scan a range of ports")

try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("Invalid input.")
    exit()

start_time = time.time()

# -------------------- Single Port --------------------
if choice == 1:
    try:
        port = int(input("Enter port number to scan: "))
    except ValueError:
        print("Invalid port number.")
        exit()

    result = scan_port(ip, port)

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

# -------------------- Scan All Ports --------------------
elif choice == 2:
    open_ports = 0

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_port, ip, port): port
            for port in range(1, 65536)
        }

        for future in as_completed(futures):
            port = futures[future]

            try:
                result = future.result()
                if result == 0:
                    print(f"Port {port} is OPEN")
                    open_ports += 1
            except Exception:
                pass

    print(f"\nTotal open ports found: {open_ports}")

# -------------------- Scan Port Range --------------------
elif choice == 3:
    try:
        sp = int(input("Enter starting port number: "))
        ep = int(input("Enter ending port number: "))
    except ValueError:
        print("Invalid port numbers.")
        exit()

    if sp < 1 or ep > 65535 or sp > ep:
        print("Invalid port range.")
        exit()

    open_ports = 0

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_port, ip, port): port
            for port in range(sp, ep + 1)
        }

        for future in as_completed(futures):
            port = futures[future]

            try:
                result = future.result()
                if result == 0:
                    print(f"Port {port} is OPEN")
                    open_ports += 1
            except Exception:
                pass

    print(f"\nTotal open ports found: {open_ports}")

# -------------------- Invalid Choice --------------------
else:
    print("Invalid choice.")

end_time = time.time()
print(f"\nScan completed in {end_time - start_time:.2f} seconds")