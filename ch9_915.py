#Lottery Analysis:

from random import choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_ticket = [3, 10, 'A', 7]
counts = 0

def generated_ticket(nums):
    lista = []
    while len(lista) < 4:
        chosen = choice(nums)
        lista.append(chosen)
    return lista

def compareTickets(my_ticket, winning_ticket):
    for elem in my_ticket:
        
        if elem not in winning_ticket:
            return False
    return True

active = True
while active:
    winning_ticket = generated_ticket(numbers)
    counts += 1
    woncounts = compareTickets(my_ticket, winning_ticket)
    if woncounts == True:
        active = False

print(counts)
print(winning_ticket)
print(my_ticket)
    

