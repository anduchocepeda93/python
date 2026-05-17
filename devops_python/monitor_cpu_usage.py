import psutil
import time

for _ in range(5):
    print("CPU:", psutil.cpu_percent(interval=1), "%")
    time.sleep(2)
