orders = [["Товар1", 1,500], ["Товар2", 7,1000],["Товар1", 6,900], ["Товар1", 3,700], ["Товар2", 7,1000],["Товар3", 2,550], ["Товар4", 7,300],["Товар5", 2,300]]
print('Список до сортировки: ')
for arr in orders:
    print(arr)

sorted_orders = sorted(orders, key= lambda x: (x[0], x[1]*x[2]))

print('Отсортированный список: ')
for arr in sorted_orders:
    print(arr)