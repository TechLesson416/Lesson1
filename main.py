# Списки (list)
# Имитация стека


N = 5

lst = [] #Пустой список

for i in range(N):
    print(f'Кладём книгу {i + 1} в стопку.')
    lst.append(i + 1)

print ('---')

while lst:
    item = lst.pop(0) # стек стоит по умолчанию
    print (f'Берём книгу {item} из стопки.')











