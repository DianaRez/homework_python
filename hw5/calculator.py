import math
import numbers


class Complex:

    def __init__(self, x = 0, y = 0):
        self.set(x, y)

    def set(self, x, y):
        if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
            self.a = x
            self.b = y
        else:
            raise ValueError


    def get(self, exp = False):
        if exp == True:
            return self.r, self.phi
        else:
            return self.a, self.b



    def convert_v_exp(self):
        if self.a == 0:
            raise Exception("convert impossible")
        self.r = (self.a**2 + self.b**2)**0.5
        if self.a < 0 and self.b > 0:
            self.phi = math.pi - math.atan(abs(self.b) / abs(self.a))
        elif self.a < 0 and self.b < 0:
            self.phi = math.pi + math.atan(abs(self.b) / abs(self.a))
        elif self.a > 0 and self.b < 0:
            self.phi = - math.atan(self.b/self.a)
        else:
            self.phi = math.atan(self.b / self.a)

        return round(self.r, 2), round(self.phi, 2)

    def convert_v_alg(self):
        if self.a == 0:
            return 0, 0
        else:
            self.r = self.a
            self.phi = self.b
            self.x = self.r * math.cos(self.phi)
            self.y = self.x * math.tan(self.phi)

            return round(self.x, 2), round(self.y, 2)

    def __add__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return self.a + other, self.b
            else:
                return self.a + other.a, self.b + other.b
        # except AttributeError:
        #     print("enter number!")

    def __radd__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return self.a + other, self.b
            return self.a + other.a, self.b + other.b
        # except AttributeError:
        #     print("enter number!")

    def __sub__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return self.a - other, self.b
            else:
                return self.a - other.a, self.b - other.b
        # except AttributeError:
        #     print("enter number!")

    def __rsub__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return other - self.a, self.b
            else:
                return other.a - self.a, other.b - self.b
        # except AttributeError:
        #     print("enter number!")

    def __mul__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return self.a * other, self.b * other
            else:
                return self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a
        # except AttributeError:
        #     print("enter number!")

    def __rmul__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return self.a * other, self.b * other
            else:
                return other.a * self.a - other.b * self.b, other.a * self.b + other.b * self.a
        # except AttributeError:
        #     print("enter number!")

    def __floordiv__(self, other):
        if isinstance(other, numbers.Number):
            return round(self.a / other.a, 2), round(self.b / other.a, 2)
        else:
            return round((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), 2), round(
                (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2), 2)

    def __rfloordiv__(self, other):
        if isinstance(other, numbers.Number):
            return round(other / self.a, 2), round(other / self.b, 2)
        return round((other.a * self.a + other.b * self.b) / (self.a ** 2 + self.b ** 2), 2), round(
            (other.b * self.a - other.a * self.b) / (self.a ** 2 + self.b ** 2), 2)


    def __str__(self, exp = False):
             return str(round(self.a, 2)) + "+i*" + str(round(self.b, 2)) + '   '+ str(round(self.convert_v_exp()[0], 2)) + '*exp^(i*' + str(round(self.convert_v_exp()[1], 2)) + ")"

    # def __str__(self):
    #     return str(round(self.a, 2)) + "+i*" + str(round(self.b, 2))

    def __eq__(self, other):
        # try:
            if isinstance(other, numbers.Number):
                return (self.a == other and self.b == 0)
            else:
                return self.a == other.a and self.b == other.b
        # except AttributeError:
        #     print("enter number!")

    def __abs__(self):
        return round((self.a**2 + self.b**2)**0.5, 2)

    def __getitem__(self, key):
        if key == 0:
            return self.a
        elif key == 1:
            return self.b
        else:
            raise ValueError

    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        elif key == 1:
            self.b = value
        else:
            raise ValueError

    def __pow__(self, power, modulo=None):

        if self.a == 0 and self.b == 0:
            if power == 0:
                raise Exception('???????? ?? ???????? ???? ??????????????????!')
            else:
                return 0, 0
        else:
            self.r, self.phi = self.convert_v_exp()
            self.r = self.r ** power
            self.phi = self.phi * power
            self.a, self.b = self.r, self.phi
            return self.convert_v_alg()



print("?????????????? ?????? ?????????????????????? ??????????: ?? ?????????????? a b c d, ?????? a ?? b ???????????????????????????? ?? ???????????? ?????????? ?????????????? ?????????? ????????????????????????????, ?? c ?? d - ??????????????.")
try:
    arr = [float(t) for t in input().split()]
except ValueError:
    print("?????????????? ??????????!")
else:
    try:
        A = Complex(arr[0], arr[1])
        B = Complex(arr[2], arr[3])
    except IndexError:
        print("???? ?????????? ?????????? 4 ??????????")

print("?????????????? ????????????????: +, -, /, *, == (?????????????????? ???????? ??????????), conv_exp  (?????????????? ?? ?????????????????????????? ?????????? ??????????????), pow  (???????????????????? ?? ?????????????? ??????????????), abs (???????????? ???????????? ???? ?????????????? ??????????)")
oper = input()
try:
    if oper not in ("+", "-", '/', '*', '==', 'conv_exp', 'pow', 'abs'):
        raise TypeError
except TypeError:
    print('?????????????? ???????????????????????????? ???????????????? ???? ????????????')


if oper == '+':
    print(A + B)
if oper == '-':
    print(A - B)
if oper == '*':
    print(A * B)
if oper == '/':
    try:
        print(A // B)
    except ZeroDivisionError:
        print('?????????????? ???? ????????! ?????????????? ???????????? ?????????????????????? ??????????!')
if oper == 'conv_exp':
    try:
        print('?????????????????????? ?????????????? ??????????:', A.convert_v_exp())
    except Exception:
        print('?????????????????????? ?????????????? ?????????? ????????????????????! ?????????????? ???????????? ?????????????????????? ??????????')
    try:
        print('?????????????????????? ?????????????? ??????????:', B.convert_v_exp())
    except Exception:
        print('?????????????????????? ?????????????? ?????????? ????????????????????! ?????????????? ???????????? ?????????????????????? ??????????')
if oper == '==':
    print(A == B)

if oper == 'abs':
    print('???????????? ?????????????? ??????????:', abs(A))
    print('???????????? ?????????????? ??????????:', abs(B))

if oper == 'pow':
    print('?????????????? ??????????????')

    try:
        power = float(input())
    except ValueError:
        print("?????????????? ??????????!")

    try:
        print('?? ?? ??????????????', power, ':', pow(A, power))
    except Exception:
          print('?????????????? ?? ???????????????????? ???? ??????????????: ???????????????? ?????????????? ?????? ???????????? ?????????????????????? ??????????')

    try:
        print('B ?? ??????????????', power, ':', pow(B, power))
    except Exception:
          print('?????????????? ?? ???????????????????? ???? ??????????????: ???????????????? ?????????????? ?????? ???????????? ?????????????????????? ??????????')











