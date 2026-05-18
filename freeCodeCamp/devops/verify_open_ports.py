import socket

def check_port(host, port):
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")
    finally:
        s.close()

check_port("google.com", 80)