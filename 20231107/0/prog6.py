NotANumber = True

while NotANumber:
    try:
        a = int(input())
    except Exception:
        print(f'Nope')
    else:
        NotANumber = False