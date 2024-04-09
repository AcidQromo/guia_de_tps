primer_parcial = float(input("Ingresa la nota de tu primer parcial: "))
segundo_parcial = float(input("Ingresa la nota de tu segundo parcial: "))

if primer_parcial >= 7 and segundo_parcial >= 7:
    print("Promociona.")
elif primer_parcial >= 4 and segundo_parcial >= 4:
    print("Aprueba, no promociona.")
else:
    print("Desaprueba. Debe recuperar.")