l1 = []
l2 = []

l1.append(list(eval(input())))
for i in range(1, len(l1[0])):
    l1.append(list(eval(input())))
for i in range(len(l1[0])):
    l2.append(list(eval(input())))

l3 = [[0] * len(l1[0]) for i in range(len(l1[0]))]
for i in range(len(l1)):
    for j in range(len(l1)):
        for s in range(len(l1)):
            l3[i][j] += l1[i][s]*l2[s][j]
    print(*l3[i], sep = ",")
