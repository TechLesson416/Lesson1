#Списочные выражения (list comprehension)
#squares = [i**2 for i in range(10)]
# squares
#fro i in range(10):
#   squares.append(i ** 2)

# список квадратов чисел
# squares = [i ** 2 for i in range(10)]


# список квадратов чётных чисел
squares = [i ** 2 for i in range(10) if i % 2 == 0]


print(*squares, sep=',')

# произведение i и j
print([i * j for i in range(3) for j in range(3)])

for i in  range(3):
        for j in range(3):
            print(i * j)

n = '100 200 300 400 500 600 700 800 900'
approved = ['500', '800']
a = [int(i) for i in n.split() if int(i) in approvred]
#какие-то действия со списком а
print(a)
