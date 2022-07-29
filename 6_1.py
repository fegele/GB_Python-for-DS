# Для оценки выбрана задача 3.8:
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# Версия и разрядность:
# print(sys.version, sys.platform)
# 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)] win32

### Изначальный вариант
# Здесь используется локальная переменная sum и четыре счётчика i, j, line, item (type=<class 'int'>, size=24|28).
# Результатом выполнения программы является список (size=120) с пятью вложенными списками (size=88), каждый из которых
# содержит четыре целых числа (size=24|28)

import sys


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level+1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level+1)


matrix = []

for i in range(5):
    matrix.append([])
    sum = 0
    for j in range(4):
        if j < 3:
            matrix[i].append(int(input(f'Введите значение элемента a{i+1}{j+1}: ')))
            sum += matrix[i][j]
        else:
            matrix[i].append(sum)
            print(f'Сумма элементов {i+1}-й строки - {sum}')

for line in matrix:
    for item in line:
        print(f'{item:>5}', end=' ')
    print()


show_size(matrix)
#  type=<class 'list'>, size=120, object=[[1, 2, 3, 6], [1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3]]
# 	 type=<class 'list'>, size=88, object=[1, 2, 3, 6]
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=2
# 		 type=<class 'int'>, size=28, object=3
# 		 type=<class 'int'>, size=28, object=6
# 	 type=<class 'list'>, size=88, object=[1, 1, 1, 3]
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=3
# 	 type=<class 'list'>, size=88, object=[1, 1, 1, 3]
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=3
# 	 type=<class 'list'>, size=88, object=[1, 1, 1, 3]
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=3
# 	 type=<class 'list'>, size=88, object=[1, 1, 1, 3]
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=1
# 		 type=<class 'int'>, size=28, object=3
