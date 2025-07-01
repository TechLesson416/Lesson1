# Списочные выражения (list comprehension)
# Занести в список каждое третье слово из предложения
text = 'Списочные выражения применяются для эффективности кода'


#res = [a for a in text.split() if (text.index(a) + 1) % 3]
res = set(a for a in text.split()[2::3])
#
print(res)
