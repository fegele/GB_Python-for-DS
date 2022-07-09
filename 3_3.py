# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

list = [random.randint(1, 99) for i in range(20)]
print(list)
index_min = 0
index_max = 0

for index, i in enumerate(list):
    if i < list[index_min]:
        index_min = index
    if i > list[index_max]:
        index_max = index

list[index_min], list[index_max] = list[index_max], list[index_min]

print(list)
