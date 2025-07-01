# Функции
# Scope (local or global)
# Синтаксис:
# def <имя функции>([параметры]):
#    команды
name = 'Пётр' # глобальная перемена
count = 0



def greet_to_name(name='noname'):

    print('Привет', name)
    print(count)



print(name)

def increment():
    global count
    cout += 1


def print_list(array=[]):
    if array is None:
        array = []
for item in array:
        print(item)

#increment()
greet_to_name('person')
print_list(['Мяу', 'Гав'])

