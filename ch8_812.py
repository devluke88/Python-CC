#Sandwiches:

def build_sandwich(*ingredients):
    print("You order a sandwich with the following ingriedients: ")
    for ingredient in ingredients:
        print("- " + ingredient)

build_sandwich('cheese')
build_sandwich('ham', 'tomato', 'basil', 'mayo')
build_sandwich('egg', 'tomato')