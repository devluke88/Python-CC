# Guest:

filename = "guest.txt"

with open(filename, 'w') as file_object:
    guest = input("What is your name? ")
    file_object.write(guest)