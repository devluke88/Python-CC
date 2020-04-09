pizzas = ['margherita', 'pepperoni', 'hawai']


# for pizza in pizzas:
#     print(f"I like {pizza} pizza!")

friend_pizzas = pizzas[:]
pizzas.append('ham')
friend_pizzas.append('sicilia')

print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")
for fpizza in friend_pizzas:
    print(fpizza)
