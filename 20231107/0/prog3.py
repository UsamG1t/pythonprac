class A: pass
class B: pass

class C(A, B): pass
# class D(B, A): pass
class D(A, B): pass

class E(C, D): pass # fault | change args in D
print(1)
class E(C, A): pass
print(2)
class E(C, B): pass
print(3)
class E(D, C): pass # fault | change args in D
print(4)
# class E(B, C): pass # fault | change args
print(5)
# class E(A, C): pass # fault | change args
print(6)