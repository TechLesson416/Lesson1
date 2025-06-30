# Списки (list)

# lst = [] # пустой список
lst = list(range(10))
slice = lst[2::2]
print(slice)
for item in range(0, len(lst), 2):
    print(lst[item], '-', item ** 2)

