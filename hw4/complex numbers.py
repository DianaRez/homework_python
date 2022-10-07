import math
import numbers


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
        if isinstance(other, numbers.Number):
            return self.a + other, self.b
        else:
            return self.a + other.a, self.b + other.b

    def __radd__(self, other):
        if isinstance(other, numbers.Number):
            return self.a + other, self.b
        return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return self.a - other, self.b
        else:
            return self.a - other.a, self.b - other.b

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return other - self.a, self.b
        else:
            return other.a - self.a, other.b - self.b

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.a * other, self.b * other
        else:
            return self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self.a * other, self.b * other
        else:
            return other.a * self.a - other.b * self.b, other.a * self.b + other.b * self.a

    def __floordiv__(self, other):
        if isinstance(other, numbers.Number):
            return round(self.a/other.a, 2), round(self.b/other.a, 2)
        else:
            return (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)

    def __rfloordiv__(self, other):
        if isinstance(other, numbers.Number):
            return round(other/self.a, 2), round(other/self.b, 2)
        return (other.a * self.a + other.b * self.b) / (self.a ** 2 + self.b ** 2), (other.b * self.a - other.a * self.b) / (self.a ** 2 + self.b ** 2)

    def __str__(self, exp = False):
            return str(round(self.a, 2)) + "+i*" + str(round(self.b, 2)) + '   '+ str(round(self.convert_v_exp()[0], 2)) + '*exp^(i*' + str(round(self.convert_v_exp()[1], 2)) + ")"

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return (self.a == other and self.b == 0)
        else:
            return self.a == other.a and self.b == other.b

    def __abs__(self):
        return (self.a**2 + self.b**2)**0.5

    def __getitem__(self, key):
        if key == 0:
            return self.a
        elif key == 1:
            return self.b

    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        elif key == 1:
            self.b = value






x = complex(1,0)
y = complex(1,5)
#x[0] = 5
#print(x[0])
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print( x==1 )
print(abs(x))
print(x*0.5)
print(5*x)
print(y)
print(0.5 + x)

x.convert_v_exp()
print(x.get())



