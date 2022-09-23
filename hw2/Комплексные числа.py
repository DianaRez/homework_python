import math
class complex:
    a = 0
    b = 0

    def __init__(self, x, y):
        self.set(x, y)

    def set(self, x, y):
        self.a = x
        self.b = y

    def get(self):
        return self.a, self.b

    def convert_v_exp(self):
        r = (self.a**2 + self.b**2)**0.5
        if self.a < 0 and self.b > 0:
            phi = math.pi - math.atan(abs(self.b) / abs(self.a))
        elif self.a < 0 and self.b < 0:
            phi = math.pi + math.atan(abs(self.b) / abs(self.a))
        elif self.a > 0 and self.b < 0:
            phi = - math.atan(self.b/self.a)
        else:
            phi = math.atan(self.b / self.a)

        return str(round(r,2))+'*exp^(i*' + str(round(phi, 2)) + ")"


    def convert_v_alg(self):
        r = self.a
        phi = self.b
        x = r * math.cos(phi)
        y = x * math.tan(phi)

        return str(round(x, 2)) + "+i*" + str(round(y, 2))


def summa(x, y):
    sum.a = x.a + y.a
    sum.b = x.b + y.b
    return str(sum.a) + "+i*" + str(sum.b)

def subtraction(x, y):
    sub.a = x.a - y.a
    sub.b = x.b - y.b
    return str(sub.a) + "+i*" + str(sub.b)

def multiplication(x, y):
    mult.a = x.a * y.a - x.b * y.b
    mult.b = x.a * y.b + x.b * y.a

    return str(mult.a) + "+i*" + str(mult.b)

def division(x, y):
    div.a = (x.a * y.a + x.b * y.b) / (y.a**2 + y.b**2)
    div.b = (x.b * y.a - x.a * y.b) / (y.a**2 + y.b**2)

    return str(round(div.a)) + "+i*" + str(round(div.b))

div = complex(0,0)
mult = complex(0, 0)
sum = complex(0, 0)
sub = complex(0, 0)
x = complex(1,1)
y = complex(1,1)

print(x.convert_v_alg())
print(summa(x,y))
print(subtraction(x, y))
print(multiplication(x, y))
print(division(x, y))


