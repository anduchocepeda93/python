from collections import Counter

with open("texto.txt") as f:
    palabras = f.read().split()

conteo = Counter(palabras)
print(conteo)
