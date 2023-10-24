from itertools import repeat
def repeater(seq, n):
    for item in seq:
        print(*list(repeat(item, n)), end = ' ')
    print()

import random
repeater((random.randrange(10) for i in range(10)), random.randrange(5))