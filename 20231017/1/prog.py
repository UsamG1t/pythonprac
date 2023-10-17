s = input().lower()
M = set()

for i in range(len(s)- 1):
    if s[i].isalpha() and s[i+1].isalpha():
        M.add(s[i] + s[i+1])
print(len(M))