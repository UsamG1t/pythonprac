# class A: 
#     def __init__(self, var):
#         self.var = var

# class B(A):
#     def __init__(self, var):
#         super().__init__(var)
#         self.otvar = var * 2


class A:
    def __str__(self):
        return 'A'
class B(A):
    def __str__(self):
        return f'{super().__str__()}:B'
class C(B):
    def __str__(self):
        return f'{super().__str__()}:C'