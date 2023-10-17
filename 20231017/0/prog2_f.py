from collections import Counter
import timeit

def count_dict(s):
    d = {}
    for word in s:
        d[word] = d.setdefault(word, 0) + 1
    return d

def count_Counter(s):
    return Counter(s)

s = input().split()
print(len(s))

cyc, time = timeit.Timer(f'count_dict({s})', globals = globals()).autorange()
print("dict: ", cyc * 1 / time)

cyc, time = timeit.Timer(f'count_Counter({s})', globals = globals()).autorange()
print('Counter: ', cyc * 1 / time)