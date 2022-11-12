def print_decorator(func):
    def wrapper(*args):
        res = func(*args)
        print(args)
        return res
    return wrapper


@print_decorator
def foo(*args):
    s = 0
    for i in args:
        s += i
    return s

print(foo(4,6,7,8,3,2,5))

# как сделать так, чтобы печаталось после выполнения программы?

