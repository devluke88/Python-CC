#Lottery
from random import choice

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
lista = []
for i in range(4):
    chosen = choice(nums)
    lista.append(chosen)
print(f"Any ticket matching these four numbers or letters wins a prize: {lista}")
print(lista)

