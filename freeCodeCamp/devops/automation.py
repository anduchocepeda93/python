import os

for file in os.listdir():
    if file.endswith(".txt"):
        os.rename(file, f"new_{file}")