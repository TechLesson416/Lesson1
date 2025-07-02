# Функция, с переиенным числом аргументов
def multy(*args):
    # print(len(args)) # подсчёт числа аргументов
    # print(args) # по индексу, либо перебором в цикле
    # if len(args) == 0
        # return 0
    # result = 1
    if not args:
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result


print(multy(1, 2, 3, 4))

# Применяем is на практике
# def print_array(array: list, start: int = None):
#     if start is not None and start > len(array):
#         return
#     if start is None:
#         start = 0
#         for i in range(start, len(array)):
            # print(array[i])

# Возврат нескольких значений из функции
# При распаковке '*" может быть только одна
def coordinates() -> tuple:
    return 5.4, 3.2, 3.8, 7.2, 4.6


x, y, *rest = coordinates() # распаковка
print(f'x = {x}, y = {y}, rest = {rest}')

*names, surname = 'Остап Сулейман Бендер'.split()
print(names, surname)

print(coordinates())







