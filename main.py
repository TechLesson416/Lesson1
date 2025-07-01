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
    (55.75, 37.5): 'Москва'
}

print(d[(55.75, 37.5)])


print(d['well'][0])
if type (d['well']) == list:
    d['well'].append('скважина')
d['plum'] = 'слива'
print(d['plum'])
del d['well']

deleted_item = d.pop('apple')

print('Удалился элемент:', deleted_item)

print('Есть ли стул в словаре')
if 'стул' in d.values():
    print('Да, есть')

print('Доступ к несуществующему ключу без "Без исключений"')
pear = d.get('pear', 'Груши нет')
print('Где груша: ', pear)





# Перебор пар "ключ-значение"
for k, v in d.items(): #d.keys()
    print(k, '->', v)

print(d.keys()) # список ключей (list)
print(d.values()) # список значений (list)
print(d.items()) # список пар (ключ значения


#print(d) - словарь целиком "как  есть"

