# Регулярные выражения (поиск по паттерну)
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)
# Квантитификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m, n} - от m до n (без пробела)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности (32767) {0,}
# + - от одного до бесконечности {1,}
import re

# pattern = r'\b\w{4}\b' # все слова из 4 символов
# pattern = r'\d' # все цифры от 0 до 9
# pattern = r'начало!\Z' # На что заканчивается
# pattern = r'[0-5][0-9]' # Две идущие подряд
# pattern = r'[а-яА-я]' # все буквы от а до я и от А до Я
# pattern = '[^ерм]' # исключить символы
# pattern = r'o{2,5}' # вытащить текст из скобок
pattern = 'Go{2,5}gle' # Google
test_string = 'Google' , 'Gooogle', 'Gooooooogle'

result = re.findall(pattern, test_string)
print(result)
# Thernary If (тернарный условный оператор)
print('Цифры есть') if result else print('Цифр нет')











# Линтерны - контролирует следование хорошим практикам
# Flake 8
# pip install flake8
# (flake8-bugbear - для нахождения  логических ошибок в коде)
# (pep8-naming - проверяет имена на соответствие pep8)
# pip install flake8-bugbear pep8-naming
# Arguments --max-complexity 10 $FileDir$/$FileName$
# Path: $FileDir$
# Advanced Options/OutputFilter: #FILE_PATH$:$LINES$






# Библиотека pymorphy
# pip install pymorphy3
# pip install -U pymorphy3-dicts-ru
# from pymorphy3 import MorphAnalyzer
#
# form = MorphAnalyzer().parse('бутылка')[0]
#
# for btl in reversed(range(99)):
#     print(f'В холодильнике {btl + 1} {form.make_agree_with_number(btl + 1).word} пива')
#     print('Возьмёмодну и выпьем')
#     if btl % 10 == 1 and btl != 11:
#         remain = 'Осталась'
#     else:
#         remain = 'Осталась'
#     print(f'{remain} {btl} {form.make_agree_with_number(btl).word} пива.')
#
#
#
# import pymorphy3
#
# morph = pymorphy3.MorphAnalyzer()
#
# print(morph.parse('пила'))
#
#
#


