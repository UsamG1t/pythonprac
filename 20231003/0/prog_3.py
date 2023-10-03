def functional(f, g):
    def h(x):
        return f(x) + g(x)
    return h

print((functional(sum, sum))([1, 2, 3]) )