class Rectangle:
    rectcnt = 0
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.__class__.rectcnt += 1

        setattr(self, f'rect_{self.rectcnt}', self.rectcnt)

        print(self)

    def __abs__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def __eq__(self, obj):
        return abs(self) == abs(obj)

    def __mul__(self, value):
        return self.__class__(self.x1 * value,
                              self.y1 * value,
                              self.x2 * value,
                              self.y2 * value)

    __rmul__ = __mul__

    def __getitem__(self, idx):
        return [(self.x1,self.y1), (self.x1,self.y2),
                (self.x2,self.y2), (self.x2,self.y1)][idx]

    def __bool__(self):
        return abs(self) != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print(f'Deleting', self)

    def __str__(self):
        return f'({self.x1},{self.y1})({self.x1},{self.y2})\
({self.x2},{self.y2})({self.x2},{self.y1}), rectcnt == {self.__class__.rectcnt}'

    