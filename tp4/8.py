sueldo = int(input("Sueldo bruto percibido: "))
antiguedad = int(input("Antiguedad en años: "))
estado_civil = input("Estado civil (S o C): ")

if estado_civil == 'S':
    incremento_antiguedad = antiguedad * (sueldo * 0.05)
else:
    incremento_antiguedad = antiguedad * (sueldo * 0.07)

sueldo += incremento_antiguedad
sueldo -= (sueldo * 0.11)
sueldo -= (sueldo * 0.03)
sueldo -= (sueldo * 0.03)

print(f"El sueldo neto resultante seria de: {round(sueldo)}$")



