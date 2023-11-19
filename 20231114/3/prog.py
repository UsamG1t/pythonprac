from string import ascii_lowercase

class Alpha:
    __slots__ = list(ascii_lowercase)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        result = []
        for name in ascii_lowercase:
            if getattr(self, name, None) != None:
                result.append(f'{name}: {getattr(self, name)}')
        return ', '.join(result)

class AlphaQ:
    dictionary = {}

    def __init__(self, **kwargs):
        
        for key, value in kwargs.items():
            if key not in ascii_lowercase:
                raise AttributeError
            self.dictionary[key] = value
        for key in set(ascii_lowercase) - set(kwargs.keys()):
            self.dictionary[key] = None

    def __setattr__(self, key, value):
    
        if key not in ascii_lowercase:
            raise AttributeError
        
        self.dictionary[key] = value

    def __getattr__(self, key):
    
        if key not in ascii_lowercase:
            raise AttributeError
        
        return self.dictionary[key]


    def __str__(self):
        result = []
        for name in ascii_lowercase:
            if self.dictionary[name] != None:
                result.append(f'{name}: {self.dictionary[name]}')
        return ', '.join(result)

import sys
exec(sys.stdin.read())
