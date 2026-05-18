import subprocess

server = "8.8.8.8"
result = subprocess.run(["ping", "-c", "2", server], capture_output=True, text=True)

if result.returncode == 0:
    print(f"{server} responde al ping")
else:
    print(f"{server} no responde")
