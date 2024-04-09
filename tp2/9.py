##Ingresan valores en formato string
binary_value = str(input("Escribe el valor en binario a transformar: "))
final_sum = 0
temp_array = []
final_array = []

for i in range(0, len(binary_value)):
    value = binary_value[i:i+1]
    temp_array.append(int(value))

inverted_array = temp_array[::-1]

print(f"Valores en array: {temp_array[::-1]}")

for i in range(0, len(binary_value)):
    final_sum += inverted_array[i] * (2 ** i)

print(f"El valor en base 10 es: {final_sum}")
