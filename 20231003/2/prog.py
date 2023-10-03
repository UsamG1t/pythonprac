def spec_sum(a, b):
    itemtype = type(a)

    if itemtype is tuple or itemtype is list:
        a = list(a)
        i = 0
        while i < len(a):
            if a[i] in b:
                a.remove(a[i])
                i -= 1
            i += 1
        return itemtype(a)
    return a - b

print(spec_sum(*(eval(input()))))
