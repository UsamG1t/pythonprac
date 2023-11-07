from collections import UserString
class DivStr(UserString):
    def __init__(self, seq = ""):
        super().__init__(seq)

    def __floordiv__(self, n):
        sublen = len(self) // n
        it_seq = []
        for i in range(n):
            it_seq.append(self[i*sublen:(i+1)*sublen])
        return iter(it_seq)

    def __mod__(self, n):
        sublen = len(self) % n
        return self[-sublen:]

import sys
exec(sys.stdin.read())
