### Вариант 2
# В этом варианте используется Numpy Array. Благодаря структуре массива Numpy можно отказаться от счётчиков при выводе
# результата. Также для вычисления суммы используется встроенная функция и значение помещается сразу в массив без
# использования переменной. Под массив выделено больше памяти - двумерный массив (size=280) из одномерных
# массивов (size=104), которые по умолчанию заполняются значениями типа float (size=32).

import sys
import numpy as np


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level+1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level+1)


matrix = np.zeros((5, 4))

for i in range(5):
    for j in range(4):
        if j < 3:
            matrix[i][j] = int(input(f'Введите значение элемента a{i+1}{j+1}: '))
        else:
            matrix[i][j] = np.sum(matrix[i])
            print(f'Сумма элементов {i+1}-й строки - {matrix[i][j]}')

print(matrix)
show_size(matrix)
#  type=<class 'numpy.ndarray'>, size=280, object=[[1. 1. 1. 3.]
#  [1. 1. 1. 3.]
#  [1. 1. 1. 3.]
#  [1. 1. 1. 3.]
#  [1. 1. 1. 3.]]
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1. 1. 1. 3.]
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=3.0
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1. 1. 1. 3.]
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=3.0
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1. 1. 1. 3.]
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=3.0
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1. 1. 1. 3.]
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=3.0
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1. 1. 1. 3.]
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=1.0
# 		 type=<class 'numpy.float64'>, size=32, object=3.0
