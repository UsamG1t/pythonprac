from functools import wraps

def type_check(our_type):
    def checker(fun):
        @wraps(fun)
        def wrapper(*args):
            check = all(isinstance(arg, our_type) for arg in args)
            if not check:
                raise TypeError(f"Args Not in type {our_type}")

            res = fun(*args)
            return res
        return wrapper
    return checker

