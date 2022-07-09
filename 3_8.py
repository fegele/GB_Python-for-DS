# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

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
