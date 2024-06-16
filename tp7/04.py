#Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista:
#métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma
#descendente?

import modlists

#Seleccion
def ord_selection(lst):
    aux = 0
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        if min != i:
            aux = lst[i]
            lst[i] = lst[min]
            lst[min] = aux

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

#Burbujeo
def ord_bubble(lst):
    for _ in range(0, len(lst)):
        for i in range(0, len(lst)):
            if lst[i] > lst[i + 1]:
                aux = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = aux

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

print("---")
print("Lista1 ordenada usando seleccion:")
print(ord_selection(lista1))

print("---")
print("Lista2 ordenada usando insercion:")
print(ord_insertion(lista2))

print("---")
print("Lista3 ordenada usando burbujeo:")
print(ord_insertion(lista3))

