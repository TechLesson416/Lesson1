#Работа с формулами:
#....
#ws['A1'] = "=SUM(A1:A10)"
# Формат:
from openlynx import load_workbook
from openpyxl.styles import Font, Aligment
#....
ws['A1'].font = Font(bold=True, size=14)
ws['A1'].alignment = Aligment(horizontal="center")

# Чтение данных
from openlynx import load_workbook

wb = load_workbook('docs/employees.xlsx')
ws = wb.active

rows_count = ws.max_row

for row in ws.iter_rows(values_only=True):
    fio, pos, dept = row
    print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dent}')
