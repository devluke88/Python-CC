#!/usr/bin/env python3

tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice','Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
 
def printTable(lista):
# find the lingest string in each of the inner lists and store max
    colWidths = [0] * len(lista)
    counter = 0
    listka = []
    for i in range(len(lista)):
        colWidths[i] = len(max(lista[i], key=len))
    for y in lista[counter]:
        for x in lista:
            if lista.index(x) == len(lista) - 1:
                print(x[counter].rjust(colWidths[lista.index(x)]) + "\n", end="")
            else:
                print(x[counter].rjust(colWidths[lista.index(x)]), end=" ")
        counter += 1
    return listka

printTable(tableData)
