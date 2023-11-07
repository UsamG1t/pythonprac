class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass


for E in [A, B, C]:
    try:
        raise E
    except C:
        print(E.__name__, 'C')
    except B:
        print(E.__name__, 'B')
    except A:
        print(E.__name__, 'A')

print()

for E in [A, B, C]:
    try:
        raise E
    except B:
        print(E.__name__, 'B')
    except C:
        print(E.__name__, 'C')
    except A:
        print(E.__name__, 'A')

print()

for E in [A, B, C]:
    try:
        raise E
    except A:
        print(E.__name__, 'A')
    except B:
        print(E.__name__, 'B')
    except C:
        print(E.__name__, 'C')
