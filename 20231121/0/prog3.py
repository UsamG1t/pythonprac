import pickle

class SerCls:
    pass
c = SerCls()
c.lst = [1, 2, 3, 4, 5]
c.dct = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
c.num = 12345
c.st = 'Это строка 12345, честно'

name = input()
with open(name, 'wb') as f:
    pickle.dump(c, f)

with open(name, 'rb') as f:
    c1 = pickle.load(f)
    print(c, c.lst, c.dct, c.num, c.st, sep = '\n\n')