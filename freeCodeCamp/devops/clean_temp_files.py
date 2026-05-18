import os

directorio = "/tmp"
for archivo in os.listdir(directorio):
    if archivo.endswith(".tmp"):
        os.remove(os.path.join(directorio, archivo))
        print("Eliminado:", archivo)
