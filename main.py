# Словари
# Частотный анализ

text ="""В Сихотэ-Алинском заповеднике обнаружен новый для науки гриб —
это второй в мире вид из редкого рода Плевромицес, обитающего 
на опавших веточках реликтового рододендрона.
"""

commas = (',','!','.','?','-',':')
for x in commas:
    text=text.replace(x,'')

lst = text.strip().lower().split().sort()
print(lst)

for item in lst:
    if them in res.keys():
        res[item] += 1
    else:
        res[item] = 1

    print('Частотный анализ слов текста')
    for k, v in list:
