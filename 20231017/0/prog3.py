exp = input()
a, b = map(int, input().split(","))


print(eval(exp, {'x': a, 'y': b}), eval(exp, {'x': b, 'y': a}), sep = "\n")
