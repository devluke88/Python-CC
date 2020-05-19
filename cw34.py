# Convert number to reversed array of digits
# Given a random number:

# C#: long;
# C++: unsigned long;
# You have to return the digits of this number within an array in reverse order.

# Example:
# 348597 => [7,9,5,8,4,3]

def digitize(n):
    lista = []
    while n > 0:
        lista.append(n % 10)
        n = n//10
    return lista