def expression_matter(a, b, c):
    first = a * (b + c)
    second = a * b * c
    third = a + (b * c)
    fourth = (a + b) * c
    fifth = a + b + c
    array = [first, second, third, fourth, fifth]
    return max(array)

test = expression_matter(1, 10, 1)
print(test)
