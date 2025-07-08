# Исключения (runtime)
# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
# else:
#   если исключения не было
# finally:
#   выполняются в любом случае
###################################################################
flag = False # открывался ли на запись

try:
    fo = open('inforamtion.txt', encoding='utf-8')
    print(fo.read())
    fo.close()
except FileNotFoundError:
    fo = open('information.txt', 'wt', encoding ='utf-8')
    flsg = True
    print('Файл не обнаружен и создан с параметрами по умолчанию')
    # with open('inforamtion.txt', 'wt', encoding='utf-8') as fo:
    #     fo.write('По умолчанию')
else:
    print('Файл открыт успешно. Читаем его')
    print(fo.read())
    fo.close()
finally:
    if flag: # если флаг был открыт на запись
        fo.write('По умолчанию')
        fo.close()
    print('Продолжаем работать.')
###################################################################







