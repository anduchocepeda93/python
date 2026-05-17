"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Welcome "+name+"!")
print("You are "+age+" years old.")
"""
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    print(f"La suma de ambos numeros es: {suma}")
    print(f"La resta de ambos numeros es: {resta}")
    print(f"La multiplicacion de ambos numeros es: {multi}")
    print(f"La division de ambos numeros es: {div}")
    print("La suma de ambos numeros es: " + str(suma))
    print("La resta de ambos numeros es: " + str(resta))
    print("La multiplicacion de ambos numeros es: " + str(multi))
    print("La division de ambos numeros es: " + str(div))
except ValueError:
    print("Por favor ingresa números enteros válidos.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")