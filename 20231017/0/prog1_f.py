from string import ascii_lowercase
import timeit
wovel = set('eyuioa')
consonant = set(ascii_lowercase) - wovel
    
def letters(string):
    return (len(set(string) & wovel), len(set(string) & consonant))

cyc, time = timeit.Timer('letters("qwertyuiop")', globals = globals()).autorange()
print(cyc * 1 / time)