import time
from functools import lru_cache

dict = {}

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        dict[func] = (time.time() - start_time)
        return res
    return wrapper

@time_decorator
def fib_din(n):
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b


def fib_rec_1(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib_rec_1(n-1) + fib_rec_1(n-2)

@time_decorator
def Fib_rec(n):
    return fib_rec_1(n)



@lru_cache(maxsize=None)
def fib_rec(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

@time_decorator
def Fib_rec_cache(n):
    return fib_rec(n)





Fib_rec(35)
Fib_rec_cache(35)
fib_din(35)

max = 0
min = 10000
for i in dict:
    if dict[i] > max:
        max = dict[i]
    if dict[i] < min:
        min = dict[i]
    else:
        middle = dict[i]

time = {"max time" : [[s for s in dict if dict[s] == max], str(max)], "middle time": [[s for s in dict if dict[s] == middle], middle], "min time": [[s for s in dict if dict[s] == min], min]}

print(time)








