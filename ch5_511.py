lista = list(range(1,10))

for val in lista:
    if val == 1:
        print("%sst" % val)
    elif val == 2:
        print("%snd" % val)
    elif val == 3:
        print("%srd" % val)   
    else:
        print("%sth" % val)