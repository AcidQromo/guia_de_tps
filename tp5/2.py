#Diseñar una función para mostrar un título filas de asteriscos, la longitud de la fila de asteriscos
#y el texto del título se recibe como parámetro. Ejemplo: titulo(“Ejercicio 3”, 15)

titulo = input("Ingrese el titulo: ")
aste = int(input("Ingrese la longitud de asteriscos: "))

def title(title, lenght):
    print(f"{'*' * lenght}\n{title}\n{'*' * lenght}")

title(titulo, aste)