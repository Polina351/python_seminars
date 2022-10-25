# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# 60 -> 2, 2, 3, 5

import math


def find_divigers(num):
    divigers = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            if num % i == 0:
                divigers.append(i)
                num /= i
    return divigers


number = int(input('Введите число: '))
divigers = find_divigers(number)
if len(divigers) == 0:
    divigers.append(number)
print(divigers)
