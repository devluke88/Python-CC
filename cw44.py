# This just a simple physics problem:

# A race car accelerates uniformly from 18.5 m/s to 46.1 m/s in 2.47 seconds. Determine the acceleration of the car and the distance traveled.

# Create a function solveit(vi, vf, t) that takes in all three values and outputs a list of acceleration and distance in format [acceleration, distance].

# Formula used:

# a = (vf-vi)/t
# d = vi*t + 0.5*a*(t**2)
# If vi > vf then it should return empty list. The solution must be rounded off to double decimal place. Example: [11.17, 79.78]

def solveit(vi, vf, t):
    a = (vf-vi)/t
    d = vi*t + 0.5*a*(t**2)
    if vi > vf:
        return []
    else:
        return [round(a, 2),round(d, 2)]