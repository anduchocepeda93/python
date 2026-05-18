import re

def validar_ip(ip):
    patron = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(patron, ip):
        return all(0 <= int(num) <= 255 for num in ip.split("."))
    return False

print(validar_ip("192.168.1.1"))  # True
print(validar_ip("999.10.10.10")) # False
