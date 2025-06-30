#Строки (immutable, iterable)
#Начало и окончание строки
#startswitch и endswith
# 1. find('подстрока', start)
# 2. find('подстрока', start) - с какого места искать

s = 'сихрофазотрон' #ищем 'о': сколько их и где находятся
ch = 'о'

numbers = set()

if ch in s:
    count = s.count(ch)
    print(f'Буква {ch} встечается в слове {s} {count} раз.')
    print('Её позиция/позиции:', end=' ')
    start = 0
    for i in range(count):
        pos = s.find(ch, start)
        numbers.add(pos)
        start += pos
        print(pos, end=' ')
else:
    print(f'Буквы \'{ch}\' нет в слове "{s}".')
