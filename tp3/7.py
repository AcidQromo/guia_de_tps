seconds_ingested = int(input("Ingrese la cantidad de segundos a transformar: "))
days = seconds_ingested / 84600
hours = (days - int(days)) * 24
minutes = (hours - int(hours)) * 60
seconds = (minutes - int(minutes)) * 60
print(f"La cantidad de {seconds_ingested} segundos es de {int(days)} dias, {int(hours)} horas, {int(minutes)} minutos y {int(seconds)} segundos.")