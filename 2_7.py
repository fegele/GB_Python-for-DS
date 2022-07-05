# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

result_1 = 0
n = int(input('Введите натуральное число: '))

for i in range(n+1):
    result_1 += i
print(f'1+2+...+n = {result_1}')

result_2 = n * (n+1) / 2
print(f'n(n+1)/2 = {result_2}')

if result_1 == result_2:
    print(f'Действительно, 1+2+...+n = n(n+1)/2')
else:
    print(f'Что-то пошло не так, результаты не равны.')
