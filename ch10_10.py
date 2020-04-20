# Common words

filename = "gutenberg.txt"
lista = []
with open(filename) as file_object:
    contents = file_object.read()
   
word = 'the'
counts = contents.count(word)
print(counts)
counts = contents.lower().count(word)
print(counts)