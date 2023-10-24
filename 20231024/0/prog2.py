def walk2d():
    x = y = 0
    dx = dy = 0
    dx, dy = yield (x, y)
    while True:
        x += dx
        y += dy
        dx, dy = yield (x, y)

it = walk2d()

print(it.send(None))
print(it.send((1, 2)))
print(it.send((2, -3)))
print(it.send((4, 8)))
print(it.send((7, 5)))
print(it.send((-14, -12)))