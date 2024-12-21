"""
Из задачи 7 доработайте списки так, чтобы в каждом из двух списков были
 элементы из другого. Переведите списки в множества. Возьмите объединение и
 пересечение.
"""
import copy

# 6 Задание
orders = [["Товар1", 1,500], ["Товар2", 7,1000],["Товар1", 6,900], ["Товар1", 3,700], ["Товар2", 7,1000],["Товар3", 2,550], ["Товар4", 7,300],["Товар5", 2,300]]

product = sorted(set(arr[0] for arr in orders))
product = dict.fromkeys(product, 0)
for arr in orders:
    product[arr[0]] += arr[1] * arr[2]
print('Задание №6')
print(product)

# 7 Задание
# создание списков товаров по цене порог 7000
print('Задание №7')
large_orders = [k for k, v in product.items() if v > 7000] 
small_orders = [k for k, v in product.items() if v < 7000]
print(f'Товары с большей суммой: {large_orders}')
print(f'Товары с меньшей суммой: {small_orders}')

#8 Задание
print('Задание №8')
temp = copy.deepcopy(large_orders)
large_orders.extend(small_orders)
small_orders.extend(temp)

large_orders = set(large_orders)
small_orders = set(small_orders)

print(f'Список 1: {large_orders}')
print(f'Список 2: {small_orders}')

print(f"Объединение множеств: { large_orders | small_orders}")
print(f"Пересечение множеств: { large_orders & small_orders}")