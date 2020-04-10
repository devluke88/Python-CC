#Great Magicians

def show_magicians(names):
    print("\nList of all magicians: ")
    for name in names:
        print(name.title())

def make_great(names):
    new_names = []
    for name in names:
        new_names.append(name + " the Great")
    return new_names

mnames = ['andrew', 'anthony', 'broly']
show_magicians(mnames)

mnames = make_great(mnames)
show_magicians(mnames)