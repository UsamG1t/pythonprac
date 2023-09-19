def SumOfDigits(n):
    summ = 0
    while n != 0:
        summ += n % 10
        n //= 10
    return summ

a = int(input())

i = 0
while i <= 2:
    j = 0
    while j <= 2:
        res = (a+i)*(a+j)
        print(f'{a + i} * {a + j} =', ":=)" if SumOfDigits(res) == 6 else res, end = " ")
        j += 1
    print()
    i += 1
