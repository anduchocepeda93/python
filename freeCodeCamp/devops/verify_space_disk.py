import shutil

total, used, free = shutil.disk_usage("/")
print("Total:", total // (2**30), "GB")
print("Usado:", used // (2**30), "GB")
print("Libre:", free // (2**30), "GB")
