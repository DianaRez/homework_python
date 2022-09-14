def fib(n):
    if n < 1:
        raise ValueError
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#считаем, что числа Фибоначчи это: 0, 1, 1, 2, 3, 5, 8, 13, 21...