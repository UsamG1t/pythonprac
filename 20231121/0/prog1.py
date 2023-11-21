name = input()

with open(name, 'rb') as inp:
    size = inp.seek(0, 2)
    inp.seek(0)

    first = inp.read(size//3).decode("UTF-8")
    second = inp.readline().decode('UTF-8')
    # print(first)
    print(first, second)
