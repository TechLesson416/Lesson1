# ООП (inheritance)
# Класс, от которого наследуем: базовый, родительский, суперкласс
# Класс, который наследуется: производный, дочерний
from Lib import Rectangle


# __call__ - экземпляр класса становится вызываемым
# (как функция)
# y = ax^2 + bx + c


class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


s = SquareFunction(1, 2, 3 )
print(s(2))

class Square(Rectangle):
    def __init__(self, width, height):
        super().__init__(side, side)
        self.side = side
        self.name = 'квадрат'

    # def perimeter(self):
    #     return self.name



s = Square(5)
print(s.area())
print(s.perimeter())
print(s.get_name())


