def array_madness(a,b):
    return sum(i**2 for i in a) > sum(j**3 for j in b)

# a = [4, 5, 6]
# b = [1, 2, 3]
a = [1, 2, 3]
b = [4, 5, 6]

test = array_madness(a, b)
print(test)