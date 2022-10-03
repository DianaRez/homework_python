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

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __radd__(self, other):
        return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __mul__(self, other):
        return self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a

    def __floordiv__(self, other):
        return (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)

    def __str__(self, exp = False):
        if exp == True:
            return str(round(self.a, 2)) + '*exp^(i*' + str(round(self.b, 2)) + ")"
        else:
            return str(round(self.a, 2)) + "+i*" + str(round(self.b, 2))

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    def __abs__(self):
        return (self.a**2 + self.b**2)**0.5







x = complex(1,1)
y = complex(1,5)
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x==y)
print(abs(x))

x.convert_v_exp()
print(x, y)


