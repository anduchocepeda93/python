def obtener_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def obtener_numero_entero_no_cero():
    while True:
        numero = obtener_numero_entero("Introduce el segundo número (no puede ser cero): ")
        if numero == 0:
            print("El número no puede ser cero. Inténtalo de nuevo.")
        else:
            return numero

# Obtener los números del usuario
numero1 = obtener_numero_entero("Introduce el primer número entero: ")
numero2 = obtener_numero_entero_no_cero()

# Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostrar los resultados
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division:.2f}")
