# PEP8 - правила именования
# c, l, O, I
# Операции над множествами
a = {3, 5, 7}
b = {3, 5, 7, 9, 11}

# Объединение множеств
c = a.union(b)
# c = a / b
print(c)

# Пересечения
c = a.intersection(b) # и там, и там
# c = a & b
print(c)

# разность множеств
c = a.symmetric_difference(b) # есть в первом, но нет во втором
# c = b + a
print(c)

#  разность множеств
c = b.symmetric_difference(a) # есть в первом, но нет во втором
# c = b - a
print(c)

# симметричная разность
c = a.symmetric_difference(b) # есть в первом, но нет во втором
# c = b ^ a
print(c)