class Point:
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

def length(a,b):
    return ((a.get_x() - b.get_x()) ** 2 + (a.get_y() - b.get_y()) ** 2) ** 0.5

class Shape:
    def __init__(self, type = 'Shape'):
        self._type = type

    def __str__(self):
        return str(self._type)

class Circle(Shape):
    def __init__(self, o, r, type = "Çircle" ):
        super().__init__(type)
        self._r = r
        self._o = o

    def area(self):
        return 3.14 * self._r ** 2

    def perimeter(self):
        return 2 * 3.14 * self._r

class Triangle(Shape):

    def __init__(self, p1, p2, p3, type = "Triangle"):
        super().__init__(type)
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def perimeter(self):
        self._dist1 = length(self._p1, self._p2)
        self._dist2 = length(self._p2, self._p3)
        self._dist3 = length(self._p1, self._p3)
        return self._dist1 + self._dist2 + self._dist3

    def area(self):
        a = self.perimeter()/2
        return (a * (a - self._dist1) * (a - self._dist2) * (a - self._dist3)) ** 0.5

class Quadrangle(Shape):

    def __init__(self, p1, p2, p3, p4, type = "Quadrangle"):
        super().__init__(type)
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._p4 = p4

    def perimeter(self):

        self._dist1 = length(self._p1, self._p2)
        self._dist2 = length(self._p2, self._p3)
        self._dist3 = length(self._p3, self._p4)
        self._dist4 = length(self._p1, self._p4)
        return self._dist1 + self._dist2 + self._dist3 + self._dist4

class Rectangle(Quadrangle):
    def __init__(self, p1, p2, p3, p4, type = "Rectangle"):
        super().__init__(p1, p2, p3, p4, type)

    def perimeter(self):
        super().perimeter()

    def area(self):
        return self._dist1 * self._dist2

class Square(Rectangle):
    def __init__(self, p1, p2, p3, p4, type = "Square"):
        super().__init__(p1, p2, p3, p4, type)

    def perimeter(self):
        super().perimeter()

    def area(self):
        super().area()

class Rhomb(Quadrangle):
    def __init__(self, p1, p2, p3, p4, type = "Rhomb"):
        super().__init__(p1, p2, p3, p4, type)

    def perimeter(self):
        super().perimeter()

    def area(self):
        return 0.5 * length(self._p1, self._p3) *  length(self._p2, self._p4)

a = Square(Point(1,1), Point(1,0), Point(0,0), Point(0,1))
print(a)
print(a.perimeter())
print(a.area())





