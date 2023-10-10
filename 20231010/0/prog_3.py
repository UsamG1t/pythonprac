def scale(a, b, A, B, x):
    coef = (x-a) / (b-a)
    return A + (B-A)*coef


from math import *
for i in range(-20, 20):
    x = scale(-20, 19, -5, 5, i)
    print(" "*int(scale(-1, 1, 0, 20, sin(x))), '*')