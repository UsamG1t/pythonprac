def repeat(n):
    def repeater(fun):
        def newfun(*args, **kwargs):
            res = fun(*args, **kwargs)
            return [res for i in range(n)]
        return newfun
    return repeater
