#Guest Book:

filename = "guest_book.txt"

while True:
    guest = input("Enter your name or 'q' if you want to quit: ")
    if guest == 'q':
        break         
    else:
        with open(filename, 'a') as file_object:
            file_object.write(guest + " your name has been added\n")
        print(f"Greeting {guest}")
