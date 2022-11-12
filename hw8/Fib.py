import time
from functools import lru_cache

def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
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

# @time_decorator
# @lru_cache(maxsize=None)
def fib_rec(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# как сделать так, чтобы сначала время без кэша, а потом с кэшом???????




