# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

leap = False
year = int(input('Введите год: '))

if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True

if leap == True:
    print('Это високосный год.')
else:
    print('Это невисокосный год.')
