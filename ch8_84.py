#Large Shirts:

def make_shirt(size="L", text="I love Python"):
    print("You have ordered " + size.upper() + "-size shirt, with the following text: " + text + ".")

test = "Where there is a will there is a way"

make_shirt()
make_shirt(size="m")
make_shirt(size="xxl", text=test)