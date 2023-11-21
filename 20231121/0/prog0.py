with open('cal', 'rb') as inp:
    size = inp.seek(0, 2)
    inp.seek(0)

    first = inp.read(size//2)
    second = inp.read()

with open('half_cal', 'wb') as outp:
    outp.write(second)
    outp.write(first)
