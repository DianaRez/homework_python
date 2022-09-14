def fib(n):
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

#считаем, что числа Фибоначчи это: 0, 1, 1, 2, 3, 5, 8, 13, 21...