def cmp(a, b):
    return (a*a)% 100 > (b*b) % 100

l = list(eval(input()))
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if cmp(l[i], l[j]):
            l[i], l[j] = l[j], l[i]

print(l)