"""
 Пользователь вводит две даты в формате ДД.ММ.ГГГГ  ЧЧ:ММ. Вывести разницу
 между датами в часах, днях (целых), минутах и секундах.
"""
from datetime import datetime

date_1 = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:CC ")
date_2 = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:CC ")

date_1 = datetime.strptime(date_1, '%d.%m.%Y %H:%M:%S')
date_2 = datetime.strptime(date_2, '%d.%m.%Y %H:%M:%S')

deff = abs(date_1 - date_2)

day = deff.days
hour = deff.seconds // 3600
minute = deff.seconds % 3600 // 60
seconds = deff.seconds % 3600 % 60

print(f'Количество дней: {day} - Часы: {hour} - Минуты: {minute} - Секунды: {seconds}')

