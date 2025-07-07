# Файлы и ОС-модуль

import  os

path = os.getcwd() # get current working directory
os.chdir(patr +'/images')


all_files = [f for f in os.listdir('.') if f.endswith('.jpg')]
os.chdir('..')
print(all_files)

#os.cndir('..') # на уровень выше
# os.chdir(path + '/fonts')
# print(os.getcwd())
#
#
#
#
#
# # "Мягкое" создание директорий (вместо mkdirs)
# #os.makedirs('libs', exist_ok=True)
#
# if os.path.exists('libs'): # проверка существования пути
#     os.rmdir('libs')




# Открытие с менеджером контекста
# with open('info.txt', 'rt+', encoding='utf-8') as fo:
#     text = fo.read()
#     lst = text.splitlines()
#     print(lst)
# Проследит, чтобы файл закрылся

#fo.write ('Хороший текст.')


# text = fo.read(11)
# fo.read(6)
# text += fo.read(7)
# print('\n А Вот, что было в файле', file=fo)
#
# text = fo.readline()
# print(text)
# text = fo.readline()
# print(text)
#
# # Построчное чтение
# while text := fo.readline():
#     print(text.rstrip('\n'))
#
# # Построчное чтение №2
# lst = fo.readlines()
# lst = list(map(lambda x: x.strip('\n'), lst))
# print(lst)
#
# fo.close()
#
# # Построчное чтение № 3
# text = fo.read()
# lst = text.splitlines()
# print(lst)







