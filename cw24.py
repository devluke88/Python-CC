# Exclusive "or" (xor) Logical Operator

def xor(a,b):
    if a == False and b == False:
        return False
    elif a == True and b == False:
        return True
    elif a == False and b == True:
        return True
    elif a == True and b == True:
        return False