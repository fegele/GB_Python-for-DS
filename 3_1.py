# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

count = [0 for _ in range(2, 9+1)]

for number in range(2, 99+1):
    for index, item in enumerate(count):
        if number % (index+2) == 0:
            count[index] += 1

for index, item in enumerate(count):
    print(f'Чисел, кратных {index+2} - {item}')
