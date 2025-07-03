# словарные выражения
# lambda <аргументы>: <выражение>
# Анонимные функции (однострочники, безымянные
# lambda-функции
#Потоковый ввод sys.stdin (Ctrl + D)

import sys
#data = sys.stdin.readlines()
data = [d.strip('\n') for d in sys.stdin.readlines()]

temp = [] # индекс строкив data и число слов в виде кортежей
for i, s in enumerate(data):
    temp.append((i, len(s.split())))

temp.sort(key=lambda x:x[1])

index = temp[0][0]
res = sorted(data[index].split())

print(*res, sep='-')

print(data)

