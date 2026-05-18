import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host, port))
        print(f"Puerto {port} abierto en {host}")
    except:
        print(f"Puerto {port} cerrado en {host}")
    finally:
        s.close()

check_port("localhost", 22)
