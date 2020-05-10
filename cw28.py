def get_real_floor(n):
    if n == 0:
        return 0
    elif n >= 14:
        return n - 2
    elif n > 0 and n < 14:
        return n - 1 
    else:
        return n
