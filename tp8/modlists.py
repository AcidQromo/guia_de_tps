import random

#Genera una lista de N valores aleatorios entre 1 y 20. 
def generate_random_list(lenght):
    lst = []
    for _ in range(lenght):
        random_number = random.randint(1, 20)
        lst.append(random_number)
    
    return lst