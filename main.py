# Строки (immutable, iterable)
    #012345
#s = 'Python'
# s[3] = 'y' error (immutable)
# Индекс может быть отрицательным (с конца)
#print ('Длина слова: {len(s)}')
#print(s[-1])


s ='язык питон'
ch = {'я', 'з', 'ы', 'к', 'п', 'и', 'т', 'о', 'н'}
v = 0 #число гласных

for ch in s:
    if ch in {'а','е','ё' 'и', 'о', 'у', 'э', 'ю', 'я', 'ы','y', 'o'}:
        if ch in 'аеёиоуыэюяyo':
            v += 1
print(f'Число гласных в слове "{s}" = {v}')
for index in range (len(s)):
    print(s[index])
    print (ch)





