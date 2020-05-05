# Take an array and remove every second element out of that array. Always keep the first element and start removing with the next element.

# Example:

# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    new_list = []
    for n, i in enumerate(my_list):
        if n % 2 == 0:
            new_list.append(i)
    return new_list

my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep']
test = remove_every_other(my_list)
print(test)