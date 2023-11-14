class Num:
    exist = set()
    def __get__(self, obj, cls):
        return obj.val if id(obj) in self.exist else 0

    def __set__(self, obj, value):
        if "real" in dir(value):
            obj.val = value
        elif "__len__" in dir(value):
            obj.val = len(value)
        self.exist.add(id(obj))

import sys
exec(sys.stdin.read())