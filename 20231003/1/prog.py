def Pareto(*X):
    X = list(X)
    i = 0
    while i < len(X):
        j = 0
        while j < len(X):
            if X[i][0] <= X[j][0] and X[i][1] <= X[j][1] and \
                (X[i][0] < X[j][0] or X[i][1] < X[j][1]):
                X.remove(X[i])
                i -= 1
                break
            j += 1
        i += 1

    return tuple(X)

print(Pareto(*(eval(input()))))

