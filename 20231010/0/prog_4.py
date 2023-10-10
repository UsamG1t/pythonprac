from math import *
def scale(a, b, A, B, x):
    coef = (x-a) / (b-a)
    return A + (B-A)*coef

wigth = 60
height = 20
N = 60
scr = [[' '] * wigth for i in range(height)]

for i in range(N):
    x = scale(0, N-1, -5, 5, i)
    y = scale(-1, 1, height//2, -height//2, sin(x))
    scr[height//2 + int(y)][i] = '*'

print("\n".join(["".join(s) for s in scr]))