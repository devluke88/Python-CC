#Learning C:

path = "blank_file.txt"

with open(path) as file_object:
    lines = file_object.readlines()
    

for line in lines:
    line = line.strip()
    print(line.replace('Python', 'C'))
