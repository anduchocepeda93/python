with open("data.txt") as f:
    line_count = sum(1 for _ in f)

print("Número de líneas:", line_count)
