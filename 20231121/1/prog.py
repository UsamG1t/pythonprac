import sys

size, tail = sys.stdin.buffer.read(1), sys.stdin.buffer.read()
tail = tail[:-1]
L = len(tail)
N = size[0]

i = 0
l = []
prev = 0
while i < N and i < L:
    now = max(prev, int(i * L / N) )
    prev = max(now + 1, int((i+1) * L / N) )
    l.append(tail[now:prev])
    i += 1
res = [size[0]]
for item in sorted(l):
    res += list(item)
res.append(b'\n'[0])
sys.stdout.buffer.write(bytes(res))
