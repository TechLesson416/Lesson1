# Функции
# Return Value
def square(num):
    return num ** 2

def even_odd(num):
    if num % 2 == 0:
        return 'Чётное'
    return 'Нечётное'
    print('Привет')



def print_string(s=None):
    if s is None:
        return
    print(s)


t = square(5)
print(even_odd(5))
print(t)
t = square(t)
print(t)