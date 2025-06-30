#Строки (immutable, iterable)
#Срез (у строки и у других коллекций, кроме set)
#[начало:окончание:шаг]

#s = input('введите строку :').strip() # 'потоп'
#if s == s[::-1]:
  #  print(f'Строка "{s}" - палиндром!')
#else:
   # print(f'Строка "{s}" - не палиндром!')
#a = 'Python'

# Город Миргород
s = 'Дорог Рим'

temp = s.lower()
city = temp[:5][::-1]
res = city + '' + temp[6:][::-1] + city

print(res.title())

