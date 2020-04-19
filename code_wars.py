n = 16
sum = 0
sum2 = 0

while n > 0:
    c = n % 10
    n = int(n / 10)
    sum += c
    
if sum > 9:
    while sum > 0:
        d = sum % 10
        sum = int(sum / 10)
        sum2 += d
    print(sum2)
else:
    print(sum)