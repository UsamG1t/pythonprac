from math import *

def Calc(s, t, u): 
    def fu(x, y):
        return eval(eval(u))

    def res(x):
        return  fu(eval(eval(s)), eval(eval(t)))
    return res

expr = input().split(",")
value = eval(input())

print(Calc(*expr)(value))