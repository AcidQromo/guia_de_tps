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
lista1 = [4,2,5,1,3]

#Seleccion
def ord_selection(lst):
    min_value = lst[0]
    print(min_value)
    aux = 0
    position = 0

    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if min_value >= lst[j]:
                min_value = lst[j]
                position = j

        if min_value != lst[i]:
            aux = lst[i]
            lst[i] = min_value
            print(min_value)
            print(lst[position])
            lst[position] = aux
            print(lst[position])
            print("---")
            print(lst)
            print("---")
            min_value = lst[j]

    return lst

print(lista1)
print(ord_selection(lista1))
