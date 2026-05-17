
import socket


def check_port(host, port):
    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((host, port))
        print(f"✅ {host}:{port} OPEN")
    except:
        print(f"❌ {host}:{port} CLOSED")
    finally:
        s.close()


check_port("google.com", 80)
