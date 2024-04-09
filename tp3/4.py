medida = int(input("Ingrese medida en metros a convertir: "))
centimetros = medida * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print("La medida en centimetros es: ", centimetros)
print("La medida en pulgadas es: ", pulgadas)
print("La medida en pies es: ", pies)
print("La medida en yardas es: ", yardas)