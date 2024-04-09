num = int(input("Ingresa el primer valor: "))
div = int(input("Ingresa el segundo valor: "))

try:
    res = num / div
    print(res)
except ZeroDivisionError:
    print("El divisor es 0. Prueba con otro valor.")