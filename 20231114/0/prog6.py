class Dsc:

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return obj._value

    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        obj._value = val


class C:
    data = Dsc()

    def __str__(self):
            return f"<{self.data}>"