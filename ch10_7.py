#Addition Calculator:


while True:
    print("Enter two numbers, confirm each one with enter.")
    first = input("First number: ")
    second = input("Second number: ")
    try:
        first = int(first)
        second = int(second)
    except ValueError:
        print("Error, one of your inputs are not numbers.")
    else:
        sum = first + second
        break

print(sum)