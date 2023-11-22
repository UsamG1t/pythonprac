while s := input():
    print(s.encode('latin1', errors = 'replace').\
        decode('CP1251', errors = 'replace'))