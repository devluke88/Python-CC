text = "The narwhal bacons at midnight."
result = []
for l in text.lower():
    num = ord(l) - 96
    result.append(num)
wynik = ""
for r in result:
    if r < 0:
        continue
    else:
        wynik = wynik + str(r) + " " 
print(wynik)