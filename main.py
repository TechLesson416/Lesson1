# Декораторы
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Функция исполнялась:{finish - start:.4f} сек.')
        return result

    return wrapper
@timeit
def test():
    time.sleep(0.8)

test()







# def logger(func):
#     counter = 0
#     def decorated_func(*args, **kwargs):
#         nonlocal  counter
#         counter += 1
#         print(counter, '->', 'Аргументы:', args,
#               'Именнованные аргументы:', kwargs)
#         result = func(*args, **kwargs)
#         print('____', 'Результат:', result)
#     return decorated_func
#
# @logger
# def make_burger(meal='говядиной', onion=False, tomato=False):
#     print('Булочка')
#     if onion:
#         print('Луковые кольца')
#     print('Котлета с', meal)
#     if tomato:
#         print('Помидоры')
#     print('Булочка')
#
# make_burger(onion=True)
#
# # g = 5
# def outer():
#     x = 5
#
#     def inner():
#         nonlocal x
#         print('Nonlocal x=', x)
#         x = 10
#
#     inner()
#     print('New x=', x)
#
#
# outer()
#
#
#
#
#
#
#
#

# def upper_case_print(old_func):
#     def new_func(*args, **kwargs):
#         case = kwargs.pop('case', None)
#         if case == 'U':
#             args_up_case = [str(arg).upper() for arg in args]
#         elif case =='L':
#             args_up_case = [str(arg).lower() for arg in args]
#         return old_func(*args_up_case, **kwargs)
#     return new_func
#
#
#
# new_print = upper_case_print(print)
# new_print('Привет, Пока')
# new_print('Привет, Пока', case='U')
# new_print('Привет, Пока', case='L')
# def answer(question):
#     return 'думайте сами'
#
#
# def dialog():
#     def answer(question):
#         if question.lower().startswith('когда'):
#             return 'Никогда'
#         else:
#             return 'Упппс'
#     question = input()
#     while question != '':
#         print(answer(question))
#         question = input()
#
# dialog()









# Погода через API
# import requests
# from PIL import Image
# import io
#
# API_KEY =
# URL =
# CITY =
#
# params = {
#
#     'q': CITY,
#     'appid': API_KEY,
#     'units': 'metric',
#     'lang': 'ru'
# }
#
# response = requests.get(URL, params=params)
# result = response.json()
#
# weather = result['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
# data = result['coords']
# ll = f'{data['lon']},{data['lat']}'
# print(ll)
#
#
# print(f'Сегодня в городе {CITY}: {weather}')
# print(f'Температура: {temperature:.1}\xB0'f'C')
# print(f'Влажность: {humidity}')
# print(f'Скорость ветра: {wind}')
# link = https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.0025,0.0025&l=map&pt={ll},pm2dgl
# image = requests.get(link).content
# if image:
#     Image.open(io.BytesIO(image)).show()

