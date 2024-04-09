edad = int(input("Ingresa tu edad: "))

if edad < 4:
    print("Gratuito.")
elif edad >= 4 and edad <= 18:
    print("Paga 500$.")
else:
    print("Paga 1000$")