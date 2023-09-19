while a := input():
    if eval(a) % 2 == 0:
        print(a)
    elif eval(a) == 13:
        break
else:                       # реагирует на break
    print("Congrats, no 13")
