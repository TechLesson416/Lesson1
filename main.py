# Iterable object
# len() - сколько элементов в объекте
a = 123456
length = len(str (a))

print (length)

word = input ('Введите слово для анализа длины:')
if not word or len(word) < 4:
        print('Вы ничего не ввели')
else:
    print ('Длина слова "' + word + ' " =', len(word))