def derive(coefficient, exponent): 
    if exponent >2:
        return str(coefficient * exponent)+ "x^" + str(exponent-1)
    else:
        return str(coefficient * exponent)+ "x^" + str(exponent)