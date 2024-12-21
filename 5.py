"""
 Пользователь вводит две даты в формате ДД.ММ.ГГГГ  ЧЧ:ММ. Пользователь
 вводит третью дату в формате  ДД.ММ.ГГГГ  ЧЧ:ММ. Определить, лежит ли дата
 внутри временного интервала, образованного первыми двумя датами.
"""
from datetime import datetime

date_1 = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:CC ")
date_2 = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:CC ")
date_3 = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ:CC ")


date_1 = datetime.strptime(date_1, '%d.%m.%Y %H:%M:%S')
date_2 = datetime.strptime(date_2, '%d.%m.%Y %H:%M:%S')
date_3 = datetime.strptime(date_3, '%d.%m.%Y %H:%M:%S')

start, end = sorted([date_1, date_2])
print(start, end)

res = True if start < date_3 < end else False 

print("Лежит в интервале" if res else "Не лежит в интервале")