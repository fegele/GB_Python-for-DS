from collections import deque

numbers_16 = {"0": 0,
              "1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "A": 10,
              "B": 11,
              "C": 12,
              "D": 13,
              "E": 14,
              "F": 15}


def sum_16(n1, n2):
    number1 = deque([i for i in n1])
    number2 = deque([i for i in n2])
    if len(number1) > len(number2):
        for i in range(len(number1) - len(number2)):
            number2.appendleft('0')
    else:
        for i in range(len(number2) - len(number1)):
            number1.appendleft('0')

    result_deq = deque()
    to_add = 0

    while number1:
        spam = numbers_16[number1[-1]] + numbers_16[number2[-1]] + to_add
        if spam > 15:
            to_add = spam // 16
            spam %= 16
        else:
            to_add = 0
        result_deq.appendleft(list(numbers_16.keys())[spam])
        number1.pop()
        number2.pop()
    if to_add > 0:
        result_deq.appendleft(str(to_add))
    result = ''
    for _ in result_deq:
        result += _
    return result


def mult_16(n1, n2):
    number1 = deque([i for i in n1])
    number2 = deque([i for i in n2])
    result_deq = deque()
    iteration = 0
    while number2:
        to_add = 0
        num1_copy = number1.copy()
        interim = deque()
        while num1_copy:
            spam = numbers_16[num1_copy[-1]] * numbers_16[number2[-1]] + to_add
            if spam > 15:
                to_add = spam // 16
                spam %= 16
            else:
                to_add = 0
            interim.appendleft(list(numbers_16.keys())[spam])
            num1_copy.pop()
        if to_add > 0:
            interim.appendleft(str(to_add))
        for _ in range(iteration):
            interim.append('0')
        if len(interim) > len(result_deq):
            for i in range(len(interim) - len(result_deq)):
                result_deq.appendleft('0')
        result_deq = deque(str(sum_16(result_deq, interim)))
        iteration += 1
        number2.pop()
    result = ''
    for _ in result_deq:
        result += _
    return result


input_num1 = input("Введите первое шестнадцатиричное число: ")
input_operation = input('Выберите операцию ("+" - сложение, "*" - умножение): ')
input_num2 = input("Введите второе шестнадцатиричное число: ")

if input_operation == '+':
    print(f'{input_num1} + {input_num2} = {sum_16(input_num1, input_num2)}')
else:
    print(f'{input_num1} * {input_num2} = {mult_16(input_num1, input_num2)}')
