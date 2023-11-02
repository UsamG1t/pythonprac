class Omnibus:
    d = {}
    names = []

    def __setattr__(self, name, value):
        if (name, id(self)) not in self.names:
            self.__class__.d[name] = self.__class__.d.setdefault(name, 0) + 1
            self.names.append((name, id(self)))

    def __getattr__(self, name):
        if (name, id(self)) in self.names:
            return self.__class__.d[name]

    def __delattr__(self, name):
        if (name, id(self)) in self.names:
            self.__class__.d[name] -= 1
            self.names.remove((name, id(self)))
    
import sys
exec(sys.stdin.read())
