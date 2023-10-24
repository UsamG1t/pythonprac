from itertools import product
print(list(f'{W}{D}' for W, D in product('ABCDEFGH', '12345678')))