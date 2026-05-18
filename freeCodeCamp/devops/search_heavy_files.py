import subprocess

result = subprocess.run(["find", "/var/log", "-type", "f", "-size", "+100M"], capture_output=True, text=True)
print(result.stdout)
