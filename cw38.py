# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.

# Example:

# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

def ordered_count(inp):
    if inp:
        n = len(inp)
        i = 0
        lista = []
        while n > 0:
            counter = inp.count(inp[i])
            tup = (inp[i], counter)
            if tup not in lista:
                lista.append(tup)
            n -= 1
            i += 1
        return lista
    else:
        return []

