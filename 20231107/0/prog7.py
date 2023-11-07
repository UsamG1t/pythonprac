def div_ab(a, b):
    try:
        c =  a / b
    except ZeroDivisionError:
        from math import inf
        return inf
    else:
        return c

