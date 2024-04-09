#a
print("Hola mundo")

#b
name = str(input("Ingresa el nombre: "))
print(f"Hola {name}")

#c
num1 = float(input("Ingresa el primer valor: "))
num2 = float(input("Ingresa el segundo valor: "))
print(f"La suma es: {num1 + num2}")
print(f"La resta es: {num1 - num2}")

#d
num1 = float(input("Ingresa el primer valor: "))
num2 = float(input("Ingresa el segundo valor: "))
num3 = float(input("Ingresa el tercer valor: "))
print(f"El promedio es: {(num1 + num2 + num3) / 3}")

#e
monto = float(input("Ingresa el monto: "))
print(f"EL IVA de ese monto seria de {monto * 0.21}.")

#f
valor = float(input("Ingresa el monto: "))
print(f"El doble es: {valor * 2}")

#g
num1 = input("Escribe tu primera variable: ")
num2 = input("Escribe tu segunda variable: ")
temp = num1
num1 = num2
num2 = temp
print(f"Primera variable: {num1}. Segunda variable: {num2}")
