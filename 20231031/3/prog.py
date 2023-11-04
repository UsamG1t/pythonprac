class Maze():
    def __init__(self, size):
        self.size = size
        self.connections = {}
        for i in range(size):
            for j in range(size):
                self.connections[(i, j)] = []
    def __setitem__(self, key, value):
        x1, y1, x2, y2 = key[0], key[1].start, key[1].stop, key[2]
        
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)):
                if value == '·':
                    if (x1, j+1) not in self.connections[(x1, j)]:
                            self.connections[(x1, j)].append((x1, j+1))
                            self.connections[(x1, j+1)].append((x1, j))
                elif value == '█':
                    if (x1, j+1) in self.connections[(x1, j)]:
                            self.connections[(x1, j)].remove((x1, j+1))
                            self.connections[(x1, j+1)].remove((x1, j))
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)):
                if value == '·':
                    if (i+1, y1) not in self.connections[(i, y1)]:
                            self.connections[(i, y1)].append((i+1, y1))
                            self.connections[(i+1, y1)].append((i, y1))
                elif value == '█':
                    if (i+1, y1) in self.connections[(i, y1)]:
                            self.connections[(i, y1)].remove((i+1, y1))
                            self.connections[(i+1, y1)].remove((i, y1))
        
    def __getitem__(self, key):
        x1, y1, x2, y2 = key[0], key[1].start, key[1].stop, key[2]
        
        routes = set()
        cur = set(self.connections[(x1, y1)])
        prev = set()

        while cur - prev:
            prev |= cur
            tmp = set(cur)
            for i in tmp:
                if i not in routes:
                    routes.add(i)
                    cur |= set(self.connections[i])
            if (x2, y2) in cur:
                return True
        return False

    def __str__(self):
        field = [['█'] * (2*self.size+1) for i in range(2*self.size+1)]
        for i in range(self.size):
            for j in range(self.size):
                field[1 + 2*j][1 + 2*i] = '·'
                for dx, dy in self.connections[(i, j)]:
                    field[1 + 2*j + (dy - j)][1 + 2*i + (dx - i)] = '·'
        return '\n'.join(map(''.join, field))

import sys
exec(sys.stdin.read())