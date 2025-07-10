class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

from math import pi

class Student:
    def __init__(self, name='Bill', univ=''):
        self.name = name
        self._company = univ