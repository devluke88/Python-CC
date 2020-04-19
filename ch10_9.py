#Silent Cats and Dogs:

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(f"Printing {filename}")
    try:
        with open(filename) as file_objects:
            contents = file_objects.read() 
    except FileNotFoundError:
        pass
    else:
        print(contents)