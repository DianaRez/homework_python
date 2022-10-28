def generator_fib(finish = None):
    k = 0
    point1 = 0
    yield point1
    point2 = 1
    yield point2
    while True:
        res = point1 + point2
        yield res
        point1 = point2
        point2 = res
        k += 1
        if k > finish - 3:
            return

for i in generator_fib(10):
    print(i)

