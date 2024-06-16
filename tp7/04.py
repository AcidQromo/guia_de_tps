#Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista:
#métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma
#descendente?

import modlists
'''
desde = int(input("Ingrese desde que numero desea generar los valores (por ejemplo 1): "))
hasta = int(input("Ingrese hasta que numero desea generar los valores (por ejemplo 20): "))

longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista1 = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista1 generada con exito.")
print(lista1)

longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista2 = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista2 generada con exito.")
print(lista2)

longitud = int(input("Ingrese el valor de numeros enteros que desea en la lista: "))

lista3 = modlists.generate_random_lst(desde, hasta, longitud)
print("Lista3 generada con exito.")
print(lista3)

'''
lista1 = [3,2,5,1,4]
lista2 = [4,6,3,2,4]

#Seleccion
def ord_selection(lst):
    
    aux = 0
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            aux = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = aux

    return lst

#Insercion
def ord_insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key

    return lst
        

print(lista1)
print(ord_selection(lista1))

print(lista2)
print(ord_insertion(lista2))

