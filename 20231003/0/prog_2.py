def primitive(n):
    return primitive(n - 1) * 2 if n else "hello"

print(primitive(6))