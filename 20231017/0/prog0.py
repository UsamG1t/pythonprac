import timeit 

def my_timeit(command):
    return timeit.Timer(command).autorange()

print(my_timeit(input()))