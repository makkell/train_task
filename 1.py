
""" 
1. Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000

"""

sum_1 = sum(i for i in range(100, 1001, 2))
sum_2 = sum(i for i in range(101, 1000, 2))

print(f'Сумма четных чисел {sum_1}')
print(f'Сумма нечетных чисел {sum_2}')