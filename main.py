# выполняется в любом случае
# Задача 1
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    index = int(input('Введите текст: '))
    if not -len(lst) < index < len(lst) - 1:
        raise Valueerror('Индекс вне диапазона')
    res = lst[index]
    print(f'Число по индексу {index}: {res}')
except AssertionError as exp:
    if exp.args[0].startswith('invalid literal'):
        print(f'Вводить надо числа, а не {exp.args[1]}')
print(exp)
# index = int(input('Введите индекс:'))
#
# print(f'Число по индексу {index}: {lst[index]}')
# if mess.startswith('Invalid literal'):
