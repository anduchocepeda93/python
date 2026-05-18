import sys
import os

archivo = sys.argv[1]
print("Tamaño:", os.path.getsize(archivo), "bytes")
