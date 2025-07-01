# Словари

#Пустой словарь
# 1. d = {}
# 2. d = dict()
# Предзаполненный словарь
d = {
    'table':['таблица', 'стол'],
    'well': ['хорошо','колодец','скважина'],
    'chair': 'стул',
    'apple': 'яблоко',
    1: 'один',
}


print(d['well'][0])
if type (d['well']) == list:
    d['well'].append('скважина')
d['plum'] = 'слива'
print(d['plum'])
del d['well']

deleted_item = d.pop('apple')

print('Удалился элемент:', deleted_item)

print('Есть ли стул в словаре')
if 'chair' in d:
    print('Да, есть')


for key in d:
    print(key, '->', d[key])

#print(d) - словарь целиком "как  есть"

