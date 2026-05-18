from collections import Counter

with open("access.log") as f:
    ips = [line.split()[0] for line in f]

for ip, count in Counter(ips).most_common(3):
    print(ip, count)
