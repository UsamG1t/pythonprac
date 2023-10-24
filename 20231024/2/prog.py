from itertools import tee, islice

def slide(seq, n):
    pos = 0
    dup = tee(seq)
    while pos < 100:
        yield from islice(dup[0], pos, pos + n)
        dup = tee(dup[1])
        pos += 1
