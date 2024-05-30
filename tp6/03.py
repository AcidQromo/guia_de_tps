#Crear una lista con N valores al azar en un rango desde y hasta ingresado también desde el
#teclado. Imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe. No utilizar la
#función min, index o find de Python, debe resolver el algoritmo, puede crear sus propias
#funciones o resolverlo sin funciones.
import random

def list_filler():
    list1 = []
    number = int(input("Ingrese un valor para ingresar en la lista o -1 para terminar: "))
    while number != -1:
        if number > 0:
            list1.append(number)
            number = int(input("Ingrese un valor positivo o -1 para terminar: "))
        else:
            number = int(input("Ingrese un valor positivo valido o -1 para terminar: "))
    return list1



list_filler(desde, hasta, longitud)