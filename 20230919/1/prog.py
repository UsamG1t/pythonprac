a = int(input())

print("A", end = " ")
if a % 50 == 0:
    print("+", end = " ")
else:
    print("-", end = " ")

print("B", end = " ")
if a % 2 == 1 and a % 25 == 0:
    print("+", end = " ")
else:
    print("-", end = " ")

print("C", end = " ")
if a % 8 == 0:
    print("+")
else:
    print("-")
