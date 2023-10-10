from math import *
def scale(a, b, A, B, x):
    coef = (x-a) / (b-a)
    return A + (B-A)*coef

def printer(scr):
    print("\n".join(["".join(s) for s in scr]))    

W, H, A, B, fun = input().split()
W, H, A, B = map(int, [W, H, A, B])
scr = [[' '] * W for i in range(H)]


x = scale(0, W-1, A, B, 0)
y = eval(fun)
minn = maxx = y

for i in range(1, W):
    x = scale(0, W-1, A, B, i)
    y = eval(fun)
    minn = y if y < minn else minn
    maxx = y if y > maxx else maxx

for i in range(W):
    x = scale(0, W-1, A, B, i)
    y = scale(minn, maxx, H-1, 0, eval(fun))
    scr[int(y)][i] = '*'
    if i > 0:
        for j in [*range(int(y) + 1, prev), *range(prev , int(y))]:
            scr[j][i-1] = '*'
    prev = int(y)

printer(scr)
