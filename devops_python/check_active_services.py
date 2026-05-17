import subprocess

result = subprocess.run(["systemctl", "is-active", "ssh"], capture_output=True, text=True)
print("Estado del servicio SSH:", result.stdout.strip())
