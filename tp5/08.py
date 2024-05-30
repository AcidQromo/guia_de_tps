#Desarrollar una función para ingresar del teclado un número entero y validar que sea positivo,
#debe retornar el valor.

numero = int(input("Ingrese el numero a evaluar: "))

def divisor(number):
    if 0 < number:
        return "El numero", number, "es positivo."
    else:
        return "El numero", number, "no es positivo."

print(divisor(numero))
