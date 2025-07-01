# Вложенные списки

#a = [1, 38.6, True, False, 'sfs', (1,2)]

#N = 3
#matrix = [
 #   [1,2,3],
 #   [4,5,6],
#    [7,8,9],
#]

#matrix = [[1]* N for _ in range(3)]
#print(matrix)

#Обход двухмерного списка (матрицы)
#count = 1
#for row in range(len(matrix)):
 #   for col in range(len(matrix[row])):
 #       matrix[row][col] = count
  #      count += 1
 #   print(matrix)
#print(matrix)

N = 4

for i in range(N):
    for j in range(start, start + N):
        table.append(j)
    matrix.append(table)
    table = []
    tart += N

print(matrix)