# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

list = [random.randint(1, 99) for i in range(20)]
print(list)
index_1 = 0
index_2 = 0

# Если минимальный/максимальный элемент встречается несколько раз в списке, при подсчёте суммы учитывается элемент с наименьшим индексом
for i in list:
    if i < list[index_1]:
        index_1 = list.index(i)
    if i > list[index_2]:
        index_2 = list.index(i)

if index_1 > index_2:
    index_1, index_2 = index_2, index_1

sum = 0
for i in list[index_1+1:index_2]:
    sum += i
print(sum)
