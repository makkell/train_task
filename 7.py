"""
 Из задачи 6 постройте два списка идентификаторов товаров так, чтобы в каждом
 не было повторений.
"""

orders = [["Товар1", 1,500], ["Товар2", 7,1000],["Товар1", 6,900], ["Товар1", 3,700], ["Товар2", 7,1000],["Товар3", 2,550], ["Товар4", 7,300],["Товар5", 2,300]]

product = sorted(set(arr[0] for arr in orders))
product = dict.fromkeys(product, 0)
for arr in orders:
    product[arr[0]] += arr[1] * arr[2]
print(product)

# создание списков товаров по цене порог 7000
large_orders = [k for k, v in product.items() if v > 7000] 
small_orders = [k for k, v in product.items() if v < 7000]

print(f'Товары с большей суммой: {large_orders}')
print(f'Товары с меньшей суммой: {small_orders}')