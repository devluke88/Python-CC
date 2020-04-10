#T-Shirt

def make_shirt(size, text):
    print("You have ordered " + size.upper() + "-size shirt, with the following text: " + text + ".")

test = "Where there is a will there is a way"

make_shirt("m", test)
make_shirt(size="l", text=test)