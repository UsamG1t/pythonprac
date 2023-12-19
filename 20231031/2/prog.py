class Triangle:
    def __init__(self, dot1, dot2, dot3):
        self.dot1 = tuple(dot1)
        self.dot2 = tuple(dot2)
        self.dot3 = tuple(dot3)

    def __abs__(self):
        res = round(0.5 * abs( (self.dot2[0] - self.dot1[0])*\
                                (self.dot3[1] - self.dot1[1]) -\
                                (self.dot3[0] - self.dot1[0])*\
                                (self.dot2[1] - self.dot1[1]) ), 3)
        return res if res else 0
        
    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def dot_in_triangle(self, dot):
        return  (((self.dot1[0] - dot[0])*(self.dot2[1] - dot[1]) -\
                    (self.dot1[1] - dot[1])*(self.dot2[0] - dot[0])) >= 0) ==\
                (((self.dot2[0] - dot[0])*(self.dot3[1] - dot[1]) -\
                    (self.dot2[1] - dot[1])*(self.dot3[0] - dot[0])) >= 0) ==\
                (((self.dot3[0] - dot[0])*(self.dot1[1] - dot[1]) -\
                    (self.dot3[1] - dot[1])*(self.dot1[0] - dot[0])) >= 0)

    def __contains__(self, other):
        p1, p2 = max(self, other, key = abs), min(self, other, key = abs)
        return abs(p2) == 0 or other is self or \
                (self.__class__.dot_in_triangle(p1, p2.dot1) and
                self.__class__.dot_in_triangle(p1, p2.dot2) and
                self.__class__.dot_in_triangle(p1, p2.dot3))

    def __and__(self, other):
        if not self or not other:
            return False
        for x, y in [(self.dot1, self.dot2), \
                        (self.dot2, self.dot3), \
                        (self.dot3, self.dot1)]:
            for u, v in [(other.dot1, other.dot2), \
                            (other.dot2, other.dot3), \
                            (other.dot3, other.dot1)]:
                a = (x[1] - y[1])/(x[0] - y[0])
                b = x[1] - a*x[0]
                c = (u[1] - v[1])/(u[0] - v[0])
                d = u[1] - c*u[0]



                if ((u[0]*a + b - u[1]) > 0) != ((v[0]*a + b - v[1]) > 0) and\
                    ((x[0]*c + d - x[1]) > 0) != ((y[0]*c + d - y[1]) > 0):
                    return True

        return False

import sys
exec(sys.stdin.read())
