#Escribir la función obtener_mes_en_texto, que devuelva una cadena que representa un mes
#expresado en letras según un número entero entre 1 y 12 recibido como parámetro. Si el
#parámetro no es válido, devolver una cadena vacía. Ejemplo: Se invoca
#obtener_mes_en_texto(4) → devuelve “Abril”.

mes = int(input("Ingrese el numero de mes entre 1 y 12: "))

def obtener_mes_en_texto(month):
    ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"][month - 1]

print(obtener_mes_en_texto(mes))