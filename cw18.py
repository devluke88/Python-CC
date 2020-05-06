def triple_trouble(one, two, three):
    lista = [one, two, three]
    max_string = len(max(lista, key=len))
    new_word = ''
    for i in range (max_string):
        print(i)
        if one[i]:
            new_word += one[i]
        if two[i]:
            new_word += two[i]
        if three[i]:
            new_word += three[i]
    return new_word

one = 'Bm'
two = "aa"
three = "tn"

test = triple_trouble(one, two ,three)
print(test)

# Test.assert_equals(triple_trouble("Bm", "aa", "tn"), "Batman")