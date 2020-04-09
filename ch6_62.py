#Favourite numbers

fn = {
    'Adam' : 7,
    'Derek' : 12,
    'Kacper' : 5,
    'Krzysiu' : 17,
    'Bartek' : 23,
}

for k, v in fn.items():
    print("Hey %s, your favorite number is %s" % (k, v))
