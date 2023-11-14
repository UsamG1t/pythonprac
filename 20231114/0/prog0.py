from functools import wraps

def debug(fun):
    @wraps(fun)
    def wrapper(*args):
        print("<", *args)
        res = fun(*args)
        print(">", res)
        return res
    return wrapper

@debug
def mult(a, b):
    '''this is mult'''
    return a * b