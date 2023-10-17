text = input().split()

d = {}

for word in text:
    d[word] = d.setdefault(word, 0) + 1

print(d)