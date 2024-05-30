#Rellenar una lista con números enteros entre 0 y 20 obtenidos al azar, La carga de datos
#termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.
#Mostrar la lista por pantalla y luego realizar resolviendo el algoritmo, sin utilizar las funciones de
#Python que resuelven el problema, se espera que sea capaz de crear sus propios algoritmos:
#a. Cambiar el elemento que se encuentra en la posición cero de la lista a la última posición
#y desplazar todos los demás elementos una posición hacia delante sin perder ningún elemento.
#Se necesita utilizar variable/s auxiliares. No utilizar una lista auxiliar.
import random

def list_filler():
    list1 = []
    i = 1
    while i != 0:
        i = random.randint(0, 20)
        list1.append(i)
    
    return list1

print(list_filler())