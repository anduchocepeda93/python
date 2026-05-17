import subprocess

result = subprocess.run(["ps", "-aux"], capture_output=True, text=True)
print(result.stdout)
