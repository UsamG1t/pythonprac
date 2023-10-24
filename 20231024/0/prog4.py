from itertools import dropwhile, islice, accumulate, count

# def gen():
#     summ = 0
#     step = 1
#     while True:
#         summ += 1 / step**2
#         yield summ
#         step += 1

# print(*islice(dropwhile(lambda x: x < 1.6, it := gen()), 10))


print(*islice(dropwhile(lambda x: x < 1.6, (accumulate(1 / i**2 for i in count(1) )) ), 10))