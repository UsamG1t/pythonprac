from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)
    

print(multiplier('5', '7', float))
print(multiplier('0.25', '7', Fraction))
print(multiplier('5', '0.7', Decimal))
print(multiplier(input(), input(), eval(input())))
