    # Файлы - набор данных, сохранённых на носителях информации определённой структуры
    # name.txt
    # t - текстовый файл (txt, html, xml)
    # b - бинарные файлы (jpg, avi, mp3)
    # w - write (запись, создаётся\удаляется)
    # a - append (запись в конец)
    # r - read - чтение

    fo = open('info.txt', 'wt', encoding='utf-8')
    print(fo.mode)
    print(fo.name)
    print(fo.encoding)

    count = fo.write('Этот текст будет в файле!')
    print('В файл записано', count, 'байт!')

fo.close()























# Пишем свои модули
# from lib import diff
#
#     def main():
#         print (summ(a)
#
#
#     if __name__== '__main__':
#
#
# print(diff(7, 3))
#
# print(__name__)

# from package1 import * # для __
# import package1
from package1 import *


print(greet('Мир!'))
print(add(3,7))
print ('Автор',)

#print(package1.module._hidden_function())






#Работа с формулами:
#....
#ws['A1'] = "=SUM(A1:A10)"
# Формат:
# from openlynx import load_workbook
# from openpyxl.styles import Font, Aligment
# #....
# ws['A1'].font = Font(bold=True, size=14)
# ws['A1'].alignment = Aligment(horizontal="center")
#
# # Чтение данных
# from openlynx import load_workbook
#
# wb = load_workbook('docs/employees.xlsx')
# ws = wb.active
#
# rows_count = ws.max_row
#
# for row in ws.iter_rows(values_only=True):
#     fio, pos, dept = row
#     print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dent}')




