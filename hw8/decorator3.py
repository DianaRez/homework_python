import numbers

def error_decorator(func):
    def wrapper(*args):
        try:
            func(*args)
        except BaseException:
            print('error')
        return ''
    return wrapper

@error_decorator
def foo(*args):
    a, b = args
    # if i in args is not numbers.Number:
    #     raise Exception
    return b/a

print(foo(0, 1))