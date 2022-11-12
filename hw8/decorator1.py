def inv_decorator(func):
    def wrapper(*args):
        a = []
        for i in args:
            a.append(i)
        for i in range((len(a))//2):
            a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
        return func(*a)
    return wrapper

@inv_decorator
def foo(*args):
    return args

print(foo(3,6,4,5,6,8,7))




