#Desarrolla una función que retorne la cantidad de divisores de un número entero positivo.

numero = int(input("Ingrese el numero a evaluar: "))

def divisor(number):
    i = 1
    counter = 0
    for i in range(1, number):
        if number % i == 0:
            counter = counter + 1
    return counter

print("La cantidad de divisores para este numero es de: ", divisor(numero))