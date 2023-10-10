from decimal import *
import decimal

def esum(N, one):
    res = type(one)(1)
    n = 1
    for i in range(1, N + 1):
        n *= i
        res += type(one)(1/n)
    return res

decimal.getcontext().prec = 60
for i in range(10, 100, 5):
    print(i, esum(i, float(1)))
    print(i, esum(i, Decimal(1)))

