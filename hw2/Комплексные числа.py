import math
class complex:

    def __init__(self, x = 0, y = 0):
        self.set(x, y)

    def set(self, x, y):
        self.a = x
        self.b = y

    def get(self, exp = False):
        if exp == True:
            return self.r, self.phi
        else:
            return self.a, self.b



    def convert_v_exp(self):
        self.r = (self.a**2 + self.b**2)**0.5
        if self.a < 0 and self.b > 0:
            self.phi = math.pi - math.atan(abs(self.b) / abs(self.a))
        elif self.a < 0 and self.b < 0:
            self.phi = math.pi + math.atan(abs(self.b) / abs(self.a))
        elif self.a > 0 and self.b < 0:
            self.phi = - math.atan(self.b/self.a)
        else:
            self.phi = math.atan(self.b / self.a)

        return self.r, self.phi

    def convert_v_alg(self):
        self.r = self.a
        self.phi = self.b
        self.x = self.r * math.cos(self.phi)
        self.y = self.x * math.tan(self.phi)

        return self.x, self.y


def nice_print(x, y, exp = False):
    if exp == True:
        return str(round(x, 2))+'*exp^(i*' + str(round(y, 2)) + ")"
    else:
        return str(round(x, 2)) + "+i*" + str(round(y, 2))


def summa(x, y):
    sum.a = x.a + y.a
    sum.b = x.b + y.b

    return sum.a, sum.b


def subtraction(x, y):
    sub.a = x.a - y.a
    sub.b = x.b - y.b

    return sub.a, sub.b



def multiplication(x, y):
    mult.a = x.a * y.a - x.b * y.b
    mult.b = x.a * y.b + x.b * y.a

    return mult.a, mult.b



def division(x, y):
    div.a = (x.a * y.a + x.b * y.b) / (y.a**2 + y.b**2)
    div.b = (x.b * y.a - x.a * y.b) / (y.a**2 + y.b**2)

    return div.a, div.b


div = complex()
mult = complex()
sum = complex()
sub = complex()
x = complex(1,1)
y = complex(1,1)

x.convert_v_exp()
print(x.get(True))
a,b = summa(x,y)
print(nice_print(a,b))
print(x.convert_v_alg())
print(summa(x,y))
print(subtraction(x, y))
print(multiplication(x, y))
print(division(x, y))


