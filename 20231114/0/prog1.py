from functools import wraps

def int_check(fun):
    @wraps(fun)
    def ich(*args):
        for arg in args:
            if type(arg) is not int:
                raise TypeError("Args must be int")

        res = fun(*args)
        return res
    return ich
