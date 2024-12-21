"""
9.Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения
"""
"""
10.Создайте метод, который выводит ФИО.
"""
"""
11.Создайте метод, который вычисляет возраст в годах.
"""
"""
12.Создайте класс - наследник вашего первого класса. Перекройте в нём метод,
 вычисляющий возраст в годах на метод, который вычисляет возраст в днях.
"""

"""
13.Создайте декоратор для метода, который выводит ФИО. Пусть новый метод
 выводит ФИО, заключенное в теги <strong>.
"""

import datetime

def strong(func):
    def wrapper(*args, **kwargs):
        return '<strong>' + func(*args, **kwargs) + '<strong>'
    return wrapper


class Human():
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year

    def full_name(self):
        return f'Имя: {self.name} Фамилия: {self.surname}'

    def age(self):
        today = datetime.datetime.today()
        return int(today.year) - self.year


class Human_heir(Human):
    def __init__(self, name, surname, year):
        super().__init__(name, surname, year)
    
    @strong
    def full_name(self):
        return super().full_name()
    
    def age(self):
        today = datetime.datetime.today()
        return (int(today.year) - self.year) * 365

print("Объект родительского класс")

man = Human("Александр", "Коренков", 2003)
print(man.full_name())

print(f"Возраст в годах: {man.age()}")

print()

print('Объект класса наследника')
man_2 = Human_heir('Александр', "Коренков", 2003)
print(man_2.full_name())

print(f"Возраст в днях: {man_2.age()}")
