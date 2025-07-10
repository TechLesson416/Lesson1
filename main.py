# ООП (magic methods)
# method override; operator overloading
from math import hypot


class Point:
    def __init__(self, x=0, y=0):
        self.x = y
        self.y = x


    def __str__(self):
        return f'<Point: ({self.x}, {self.y})>'

    def __repr__(self):
        return f'<List of Point: ({self.x}, {self.y})>'

    def __sub__(self, other):
        return Point(abs(self.x - other.x, self.y - other.y))

    def __add__(self, other):
        return hypot (self.x - other.x, self.y - other.y)


    # return Point(abs(self.x - other.x), abs(self.y - other.y))


    #p = Point
    p1 = Point(5, 7)
    p2 = Point(9, 12)
    print(p1 - p2)
    print(p1 + p2)
    # str(a) -> a.__str__()







# isinstance(объект, тип) -> True
# isinstance(объект, (тип1, тип 2, тип N)) -> True

# lst = list(range(1, 15))
# lst += ['a']
#
#
# class Stat:
#     def __init__(self, vals):
#         self.values = vals[:] # получаем копию
#
#     def is_all_int(self):
#         return all(ininstance(item, int) for item in self.values)
#
#     def get_min(self):
#         if self.is_all_int():
#            return min(self.values)
#         return None
#
#     def get_max(self):
#         if self.is_all_int():
#            return max(self.values)
#         return None
#
#     def get_aver(self):
#         if self.is_all_int():
#            return min(self.values)
#         return None
#
#
# s = Stat(lst)
# print(s.get_min())
# print(s.get_max())
# print(s.get_aver())
#
#
#
#
# s = Selector(lst)
# print(s.get_odd())
# print(s.get_even())
# print(lst)


# from lib import Student, Employee, Person
#
# people = [
#     Person('Александр', 27),
#     Student('Дмитрий', 'ГУАП'),
#     Employee('Пётр','Авангард')
#
# ]
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_university())
#     elif isinstance(person, Employee):
#         print(person.get_company())
#     else:
#         print(person.get_name())