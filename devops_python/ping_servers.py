import subprocess

servers = ["8.8.8.8", "1.1.1.1", "localhost"]

for server in servers:
    result = subprocess.run(["ping", "-c", "1", server], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"{server} está activo")
    else:
        print(f"{server} no responde")
