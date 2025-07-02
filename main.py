# Функция, как объект
# Передаётся вдругие функции: функции высшего порядка

# Функция критерия отбора элементов списка
# Критерий: длина слова
def is_longer_six(word):
    return len(word) > 6



# Критерий - первая буква
def if_first_lette_a(word):
    return word[0] == 'a'

def square(num):
    return num ** 2

nums = [1,2,3,4,5,6,7,8,9] #123456789
squares = map(square, nums)
print(list(squares))



words = ['В','этом', 'списке', 'останутся', 'слова',
         'длина', 'которых', 'больше', 'шести']

fruits = list(filter(is_longer_six, words))
print(result)


result = list(filter(is_longer_six, fruits))
print(result)

for word in filter(is_longer_six, words):
    print(word)















#
# def print_any(*args, **kwargs):
#     for i in args:
#         print(i)
#     for k, v in kwargs.items():
#         print(k, '=', v)
#
# def profile(name, surname, city, *children, **additional):
#      print(f'Имя:', {name})
#      print(f'Фамилия: {surname}')
#      print(f'Из города: {city}')
#      if len(children) > 0:
#          print('Дети:',','.join(children))
#      if 'hobbie' in additional:
#          print('Хобби:',','.join(additional['hobbie']))
#     #print(additional)
#
#     profile('Дмитрий', 'Колесов', 'Волгоград',
#     'Мария','Пётр',hobbie=['Филателия', 'Шахматы'])
#
#


