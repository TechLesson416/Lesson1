#Строки
#Создаём алфавит

alphabet ='абвгджзеёклмнопрстуфчшщъыьэюя'
#alphabet += alphabet.upper()
#alphabet_u = alphabet.upper()

#Получаем входные данные
message = input('Введите строку: ').strip().lower()
key = int(input('Введите ключ: '))


#Инициализируем пустую строку для результата
encrypted = ''


#Перебираем каждый символ в сообщении
for letter in message:
    #Проверяем, является ли символ буквой из алфавитва
    if letter in alphabet:
        #Находим позицию буквы в алфавите
        t = alphabet.index(Letter)
        #Вычисляем новую позицию с учётом сдвига
        new_key = (t + key) % len (alphabet)
        #Добавляем зашифрованный символ
        encrypted += alphabet[new_key]
    else:
        #Если символ не буква, оставляем его без изменений
        encrypted += letter

    # Для расшифровки достаточно изменить формулу вычисления позиции:
    # new_key = (t - key) % len(alphabet)

    print('Зашифрованное сообщение: ', encrypted)
