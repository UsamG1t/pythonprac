def travel(n):
    for i in range(n):
        yield 'По кочкам\n'
    return 'И в яму\n'

def travelwrap(n):
    action = yield from travel(n)
    yield action

n = int(input())
it = travelwrap(n)
for i in range(n + 1):
    print(next(it))
