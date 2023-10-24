def gen():
    summ = 0
    step = 1
    while True:
        summ += 1 / step**2
        yield summ
        step += 1
g = gen()
print(*[next(g) for i in range(15)], sep = '\n')