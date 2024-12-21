"""
2. Пользователь вводит дату в формате ДД.ММ.ГГГГ. Вывести первый день месяца,
последний день месяца, сам месяц.
"""

import locale
import calendar
locale.setlocale(locale.LC_TIME, "RUS")


def date(date:str):
    date = date.split('.')
    _, last_day  = calendar.monthrange(int(date[2]), int(date[1]))
    return f'\nПервый день месяца {1} - Последний день месяца {last_day} - Месяц {(calendar.month_name)[int(date[1])]}'

print(date(input('Введите дату в формате ДД.ММ.ГГГГ :')))