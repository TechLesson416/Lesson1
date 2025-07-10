# ООП (polymorhism)
# method override; operator overloading
# From lib import Book

# isinstance(объект, тип) -> True
# isinstance(объект, (тип1, тип 2, тип N)) -> True


# from lib import Circle, Rectangle, Square
#
#
# # class Circle:
# #     def __init__(self, radius):
# #         self.radius = radius
# #
# #     def perimeter(self):
# #         return (2 * pi * self.radius, 2)
# #
# #     def area(self):
# #         return (pi * self.radius ** 2, 2)
# #
# #     def get_name(self):
# #         return self.side
# #
# #
# # class Square:
# #     def __init__(self, side):
# #         self.side = side
# #
# #     def perimeter(self):
# #         return 4 * self.side
# #
# #     def area(self):
# #         return self.name
# #
# # def shape_info(shape: object):
# #     print(f'Площадь {shape.get_name()}a: {shape.area()}, Периметр: {shape.perimeter()}')
#
#
# rect, c, sqr = ['прямоугольник', 'круг', 'квадрат']
# fig = ''
#
# def shape_info(shape: object):
#     if isinstance(shape, Circle):
#         fig = c
#     if isinstance(shape, Circle):
#         fig = rect
#     if isinstance(shape, Circle):
#         fig = sqr
#     print(f'Площадь {fig}a: {shape.area()}, Периметр: {shape.perimeter()}')
#




# s = Square(10)
# shape_info(s)
#
# cr = Circle(10)
# shape_info(cr)
#
# r = Rectangle(5, 2)
# shape_info(r)
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width =  width
#         self.height = height
#         self.name = 'квадрат'
#
#     def perimeter(self):
#         return self.width * self.height
#
#
#     # def area(self):
#     #     return self.width ** 2
# #
# def shape_info(shape: object):
#     print(f'Площадь {shape.area()}a: Периметр: {shape.perimeter()}')
#









print(dir(s))
print(dir(cr))









# book = Book('Язык C++', 'Бьярн Страупструп')
#
# print(f'{book.get_title(), book.get_author()}')


# Полиформизм - это свойство кода работать с разными типами данных



# print(1 + 2)
# print(1 + 2.0)
# print('abc' + 'def')
# print([1, 2] + [3, 4])
#
# def func(x, y):
#     return x + y
#
# print(func(2,3.0))