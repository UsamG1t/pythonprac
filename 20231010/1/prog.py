from fractions import Fraction
def checker(s, w, *items):
    s = Fraction(s)
    w = Fraction(w)
    
    A = B = Fraction(0)

    i = 0
    a_deg = int(items[i])
    i += 1
    while a_deg >= 0:
        A += Fraction(items[i]) * s**a_deg
        i += 1
        a_deg -= 1

    b_deg = int(items[i])
    i += 1
    while b_deg >= 0:
        B += Fraction(items[i]) * s**b_deg
        i += 1
        b_deg -= 1

    return A/B == w

print(checker(*input().split(",")))
