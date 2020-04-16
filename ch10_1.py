#Learning Python:

blankfile = 'blank_file.txt'

print("\n---Printing as the whole file---")
with open(blankfile) as file_object:
    lines = file_object.read()
print(lines)

print("\n---Printing as looping over the lines---")
with open(blankfile) as b:
    for line in b:
        print(line.rstrip())

print("\n---Printing lines in a list--")
with open(blankfile) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

