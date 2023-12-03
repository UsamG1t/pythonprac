import inspect
class dump(type):
    def __init__(cls, name, parents, ns, **kwds):
        def decor(name):
            def dump_dec(fun):
                def wrapper(self, *args, **kwargs):
                    print(f'{name}: {tuple(args)}, {kwargs}')
                    return fun(self, *args, **kwargs)
                return wrapper
            return dump_dec

        for item in dir(cls):
            if isinstance(eval(f'cls.{item}'), type(decor)):
                exec(f'cls.{item} = decor("{item}")(cls.{item})')

        return super().__init__(name, parents, ns)

import sys
exec(sys.stdin.read())
