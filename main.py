#ENGLISH_ABC = [chr(ch) for ch in range(ord('a'),ord('z')+1)]
#print(ENGLISH_ABC)
#RUSSIAN_ABC - [chr(ch) for ch in range(ord('а'), ord('я')+1)] + ['ё']
#print(RUSSIAN_ABC)
# словарные выражения
# lambda <аргументы>: <выражение>

numbers = [1, 2, 3, 4, 5] # list(range 1, 6)
squares = {n: n ** 2 for n in numbers}
print(squares)

numbers = range (1, 11)
squares = {n: n ** 2 for n in range(1, 10) if n % 2 == 0}
print (squares)

source_dict = {
    'x': 1,
    'y': 2,
    'z': 3,
}

dest_dict = {k: v * 2 for k, v in source_dict.items()}
print(dest_dict)



# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'),ord('z')+1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'),ord('я')+1)] + ['ё']
# ABC = set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^ set([x.upper() for x in ENGLISH_ABC])
# print(ABC)
# # print(ENGLISH_ABC)
# # print(RUSSIAN_ABC)
# txt = 'Однажды, теперь и потом'.lower()
#
#
# def remove_punctuation(txt):
#
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, txt))
#
#
# print(remove_punctuation(txt)(txt))
#
# def get_words(txt: str) -> filter:
#     return remove_punctuation(txt).split()
#
# def long_words(txt, length=4) -> filter:
#     return filter(lambda word: len(word) >= length, get_words(txt))
#
# print(long_words(txt))
