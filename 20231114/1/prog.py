def objcount(cls):
    class Wrap(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            if '__init__' in dir(cls):
                super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        def __del__(self):
            self.__class__.counter -= 1

            if '__del__' in dir(cls):
                super().__del__()

    return Wrap

import sys
exec(sys.stdin.read())
