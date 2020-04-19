#Addition:

try:
    print("Enter two numbers, confirm each one with enter.")
    first = int(input("First number: "))
    second = int(input("Second number: "))
except ValueError:
    print("Error, one of your inputs are not numbers.")
else:
    sum = first + second
    print(sum)