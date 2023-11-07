class A:
    def __init__(self, var):
        self.var = var
    def __add__(self, number):
        return self.__class__(self.var + number)

class B(A):
    def __str__(self):
        return f'<{self.var}>'