from itertools import product
print(*list(filter(lambda string: string.count('TOR') == 2, (''.join(word) for word in product("TOR", repeat=int(input()) ) ) )), sep = ', ')
