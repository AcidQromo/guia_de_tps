#Rellenar una lista con números enteros entre 0 y 20 obtenidos al azar, La carga de datos
#termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.
#Mostrar la lista por pantalla y luego realizar resolviendo el algoritmo, sin utilizar las funciones de
#Python que resuelven el problema, se espera que sea capaz de crear sus propios algoritmos:

#a. Cambiar el elemento que se encuentra en la posición cero de la lista a la última posición
#y desplazar todos los demás elementos una posición hacia delante sin perder ningún elemento.
#Se necesita utilizar variable/s auxiliares. No utilizar una lista auxiliar.

#b. Rotar una posición de la lista a derecha. Igual que el punto b pero hacia la derecha.
import random

def list_filler():
    list1 = []
    i = random.randint(1, 20)
    while i != 0:
        list1.append(i)
        i = random.randint(0, 20)
    
    return list1

def first_value_2_end(list):
    first_value = list[0]

    for i in range(1, len(list)):
        list[i - 1] = list[i]
    
    list[len(list) - 1] = first_value

    return list

def last_value_2_start(list):
    last_value = list[len(list) - 1]

    for i in range(len(list) - 1, 0, -1):
        list[i] = list[i - 1]
    
    list[0] = last_value

    return list

lista = list_filler()
print("Lista sin modificaciones")
print(lista)

print("Ejercicio A")
print(first_value_2_end(lista))

print("Ejercicio B")
print(last_value_2_start(lista))

