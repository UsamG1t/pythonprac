import random, struct
random.seed(1)

name1 = input()
name2 = input()
with open(name1, 'wb') as f1:
    with open(name2, 'wb') as f2:
        for i in range(10):
            b = random.random()+random.randrange(100500),\
                random.randbytes(3), random.randrange(100500)
            f1.write(struct.pack('<f3si', b[0], b[1], b[2]))
            f2.write(struct.pack('!f3si', b[0], b[1], b[2]))
