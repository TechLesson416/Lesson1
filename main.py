# Списки (list)
# Создание аббревиатур

lst = []

while (word := input ('Введите слово: ')).strip().capitalize != '':
    lst.append(word[0].upper())

print('Получилась аббревиатура', end=': ')
print(*lst[:10], sep='')












