#Rivers

rivers = {
    'nile' : 'egypt',
    'vistula' : 'poland',
    'amazon' : 'brasil',
}

for k, v in rivers.items():
    print("The %s runs through %s" % (k.title(), v.title()))
for k in rivers.keys():
    print(k.title())

for v in rivers.values():
    print(v.title())