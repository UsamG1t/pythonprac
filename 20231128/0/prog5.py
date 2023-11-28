class Etalon:
    a, b, c = input().split()

while s := input():
    match s.split():
        case [Etalon.a, *words] if 'yes' in words:
            print('case1')
        case [Etalon.b]:
            print('case2')
        case [Etalon.c, *words, Etalon.b]:
            print('case3')
