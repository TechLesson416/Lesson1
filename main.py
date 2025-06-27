# коллекции (set, list, dict, tuple)
# Множества
# print (dir(s))
s = set() # пустое множество
s = {'3', '5', '7', '3', '3', 3}
s.add('8,5') # добавлени
s.remove ('3') # вызывает ошибку, если нет
s.discard ('3') # удаляет вслепую
s.clear() # очищает множество
temp = s.pop(5) # даляет случайный и возвращает его
print (temp)
print (dir(s))
print(type (s)) # класс
print (f'Число элементов в s = {len(s)}')
print ('Присутствуюет ли 3')
if '3' in s:
    print('Да')
else:
    print ('Нет')
for item in s:
    print (item)

if s:








