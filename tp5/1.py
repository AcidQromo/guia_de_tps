#Dado un número entero, calcular su factorial. Ejemplo: fact(4) = 4*3*2*1 = 24.

number = int(input("Ingrese el valor a analizar: "))

def fact(value):
    i = 1
    cont = 1
    for i in range(1, value + 1):
        cont = cont * i
        i = i + 1
    return cont

print(fact(number))
