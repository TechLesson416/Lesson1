# Анонимные функции (Анонимыне однострочники, безымянные)
# lambda-функции
# Lambda <аргументы>: <выражение>




# is_longer_six = lambda word: len(word ) > 6
# # Критерий - первая буква
# def is_first_letter_a(word):
#     return word[0] == 'a'
#
# is_first_letter_a = lambda word: word[0] == 'a'
#
# # Критерний - вхождение подстроки
# # в частности 'ан'
# def string_contains(s):
#         return 'ан' in s
#
# string_contains = lambda s: 'ан' in s
#
# words = []
#
# fruits = ['арбуз','ананас','банан','ежевика','малина']
#
# result = list(filter(lambda word: len(word)) > 6, words)
# print(result)
#
# res + list(filter(lambda x: x[0] == 'a', fruits))
# print(res)

#res + list(filter(lambda s: 'ан' in s, fruits))
#print(res)

# в одну строоку вывести список квадратов чисели от 3 до 15
# [9, 16, 25...]

#res = list(map(lambda y: y** 2, range (3, 16)))
res = [y ** 2 for y in range(3, 16)]
print(res)

long_words = [word for word in words if len(word) > 6]
print(long_words)

res + list(filter(lambda > 6, ))

