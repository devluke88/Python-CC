

def countBinary(n):
    count = 0
    while n > 0:
        r = n % 2
        n = n / 2
        if int(r) == 1:
            count += 1

    return count

test = countBinary(156)
print(test)