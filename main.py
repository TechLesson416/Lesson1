# Строки (immutable, iterable)
# Таблица символов
#s = '\xB0'
# = '\u2603'


#две удобные функции
# ord(символ) - возвращает код символа в Unicode
# chr(код) - возвращает код символа по Unicode-коду

#print(u)
#print('25' + s + 'С')
#print('Код снеговика в Unicode: {ord('')}')
#print(chr(10000))
#print(chr(176)) #ASCII и Unicode


s = set()
word = input ('Введите фразу для зашифровки: ')

for ch in word:
    s.add(ord(ch))

print(s)

res = ''
for i in s:
    res += chr(i)

print(res)