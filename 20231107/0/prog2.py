class A:
    __f = 1

    def __str__(self):
        return f'{self.__f}'

class B(A):
    def __init__(self):
        self.__f = 100500
