def lin(a, b):
    return lambda x: a*x + b

res = lin(2, 5)
print(res(3))
print(res.__closure__, res.__closure__[0].cell_contents, res.__closure__[1].cell_contents)