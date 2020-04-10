#Magicians

def show_magicians(names):
    print("\nList of all magicians: ")
    for name in names:
        print(name.title())

mnames = ['andrew', 'anthony', 'broly']

show_magicians(mnames[:])