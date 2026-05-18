frase = input("Ingresa una frase, y te calculo cuanto tardarias diciendola: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

persona_normal = cantidad_de_palabras/2
dalto = persona_normal * 0.3
dalto2 = persona_normal - dalto
print(f"Dijiste {cantidad_de_palabras} palabras y te tardarías {persona_normal} segundos en decirlas")
print(f"Dalto tardaría {dalto2} segundos en decirlas")

if cantidad_de_palabras >= 12:
    print("hablas demasiado mi loco")
else:
    print("hablas poco, me gusta ah!")    