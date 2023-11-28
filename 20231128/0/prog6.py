import inspect
class Checker:
    a: int
    def __init__(self, x):
        if not isinstance(x, inspect.get_annotations(self.__class__)['a']):
            raise TypeError("Type is not same with annotation")    
        self.a = x
