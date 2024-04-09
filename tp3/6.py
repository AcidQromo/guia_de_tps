anio = int(input("Ingrese el año a analizar: "))

if ((anio / 4) - int(anio / 4)) == 0 and ((anio / 100) - int(anio / 100)) == 0 and ((anio / 400) - int(anio / 400)) == 0:
    print("Es un año biciesto.")
elif ((anio / 4) - int(anio / 4)) == 0 and ((anio / 100) - int(anio / 100)) != 0:
    print("Es un año biciesto.")
else:
    print("No es un año biciesto.")
