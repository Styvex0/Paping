import socket
import time
from colorama import Fore


def ping():
    print(Fore.RED +"IP:")
    ip = input().strip()
    print(Fore.RED +"Port:")
    port = int(input().strip())
    print(Fore.RED +"Protocol (TCP/UDP):")
    protocol = input().strip().upper()

    if protocol not in ["TCP", "UDP"]:
        print(Fore.RED +"Invalid protocol. Please enter TCP or UDP.")
        return

    while True:
        if protocol == "TCP":
            result = ping_tcp(ip, port)
        else:
            result = ping_udp(ip, port) 

        if result:  
            print(f"Connected to {Fore.LIGHTGREEN_EX}{ip}{Fore.RESET} time={Fore.LIGHTGREEN_EX}{result:.3f}ms{Fore.RESET} protocol={Fore.LIGHTGREEN_EX}{protocol}{Fore.RESET} port={Fore.LIGHTGREEN_EX}{port}{Fore.RESET}")
        
        time.sleep(0.5)

def ping_tcp(ip, port):
    try:
        start_time = time.time()
        sock = socket.create_connection((ip, port), timeout=5)
        end_time = time.time()
        sock.close()
        return (end_time - start_time) * 1000  # Convert to milliseconds
    except Exception as e:
        print(f"Error: {e}")
        return None

def ping_udp(ip, port):
    try:
        start_time = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)
        sock.sendto(b'', (ip, port))
        sock.recvfrom(1024)
        end_time = time.time()
        sock.close()
        return (end_time - start_time) * 1000  # Convert to milliseconds
    except Exception as e:
        print(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    ping()
