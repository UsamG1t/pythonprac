import random, struct
random.seed(1)

name = input()
with open(name, 'wb') as f:
    for i in range(10):
        a = struct.pack('>f3si', random.random()+random.randrange(100500),\
            random.randbytes(3), random.randrange(100500))
        print(a)
        f.write(a)
