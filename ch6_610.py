#Favourite numbers

fn = {
    'Adam' : [7, 18],
    'Derek' : [12, 15, 6],
    'Kacper' : [5],
    'Krzysiu' : [17, 12, 47, 15],
    'Bartek' : [23, 24],
}

for name, numbers in fn.items():
    print("\n" + name.title() + "'s varoite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
