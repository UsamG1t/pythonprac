l = []
while a := input():
    l.append(eval(a))

w = len(l)

if all([len(el) == w for el in l]):
    for i in range(len(l) ):
        for j in range(i, len(l)):
            l[i][j], l[j][i] = l[j][i], l[i][j]

for i in l:
    print(*i)