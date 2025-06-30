# Кортеж  (tuple, immutable)
# Студент и средний балл

#N = 3
#student = []

#for _ in range(N):
    #student, average = input('ФИО: '), float(input('Ср. балл: '))
    #student.append((student, average))

#print(student)

#for st in students:
   # student, average = st
   # print('Студент: ', student)
   # print('Средний балл: ', average)


# Функция sorted() - возвращает сортированный список

s = {'Крутов','Селезнёв', 'Митрофанова'}
r = True


lst = sorted(s, reverse=r)

print(*lst, sep=',')


#lst = List(s)
#lst.sort()

#print(*lst, sep=',')





