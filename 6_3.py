### Вариант 3
# Здесь тип значений по умолчанию внутри массива Numpy был изменён на более компактный int16. В результате получился
# массив (size=160) из массивов (size=104) шестнадцатибитных чисел (size=26). Итоговый массив всё ещё занимает больше
# памяти, чем двумерный список в первом варианте, но преимуществом данного варианта является меньшее количество
# используемых переменных и счётчиков, а также в целом более высокая скорость обработки Numpy массивов.

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


matrix = np.zeros((5, 4)).astype(np.int16)

for i in range(np.size(matrix, axis=0)):
    for j in range(np.size(matrix, axis=1) - 1):
        matrix[i][j] = int(input(f'Введите значение элемента a{i+1}{j+1}: '))
    matrix[i][-1] = np.sum(matrix[i])
    print(f'Сумма элементов {i+1}-й строки - {matrix[i][j]}')


print(matrix)
show_size(matrix)
#  type=<class 'numpy.ndarray'>, size=160, object=[[1 1 1 3]
#  [1 1 1 3]
#  [1 1 1 3]
#  [1 1 1 3]
#  [1 1 1 3]]
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1 1 1 3]
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=3
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1 1 1 3]
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=3
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1 1 1 3]
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=3
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1 1 1 3]
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=3
# 	 type=<class 'numpy.ndarray'>, size=104, object=[1 1 1 3]
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=1
# 		 type=<class 'numpy.int16'>, size=26, object=3
