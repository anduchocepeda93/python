
import psutil
import socket
import subprocess

# CPU Check
cpu = psutil.cpu_percent(interval=1)
print("CPU:", "OK" if cpu < 80 else "HIGH")

# Memory Check
mem = psutil.virtual_memory().percent
print("Memory:", "OK" if mem < 80 else "HIGH")

# Port Check

def check_port(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
        return "OPEN"
    except:
        return "CLOSED"
    finally:
        s.close()

print("Port 80:", check_port("google.com", 80))
print("Port 443:", check_port("google.com", 443))

# Ping check
try:
    result = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True)
    if result.returncode == 0:
        print("Google: REACHABLE")
    else:
        print("Google: UNREACHABLE")
except:
    print("Ping failed")
