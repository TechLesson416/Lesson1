# Протокол - Совокупность правил, которые регламентируют функции передачи данных между компонентами компьютерных сетей

# Протоколы
# (TCP) - Transmission Control Protocol (Протокол управления передачей)
# Internet Protocol (IP) - разбивает на пакеты (IP-дейтаграммы), определяет их направление
# TCP/IP
# HTTP(S) - Hyper Text Trans Protocol (Формат HTML) (S - Secured)
# http://www. - Браузерный протокол
# FTP - File Transfare Protocol
# SMTP - Simple Mail Transfer Protocol
# Хост-системы - Компьютер, являющийся частью системы, к которой подключаются другие компьютеры
# Кодировки Хост-системы:
# 1. Обязательная (Дружественная компьютеру, но не человеку) - IP-адрес: 195.34.32.11
# 2. Необязательная (Наоборот^) - DNS (Domain Name System)
# http(s)://www.yandex.ru//
# ASCII %20
# URL - Uniform Resource Locator
# whois.
# nic.ru
# reg.ru
# http(s)://домен.зона/page1/?param1=value1&param2=value2


# Командная строка
# dir - листать содержание каталога и прочее
# ../images/
#rm - (remove) r templates - переход в директорию templates и удаление файлов без возможности восстановления
#cp (copy) - источник, копирование файла вдругую директорию
#mk dir - создать директорию
#cd - change directory
#mv - move
# import sys
#
# print ('Я', sys.argv[0], 'и мой аргумент', sys.argv[1])
#
#
# if len(sys.argv) >= 2:
#     match sys.argv[1]:
#         case 'p':
#             print('Привет')
#         case 'g':
#             print('Пока')
#         case _:
#             print('Не понял')


# Периодические задачи
import schedule
import datetime

i = 1

def job():
    global i
    print(f'Скрипт запустился {i}-раз')
    i += 1
    t = datetime.datetime.now()
    print('Время:', t.strftime('%H:%M:%S'))


schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()

















