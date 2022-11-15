#  Задан массив из случайных цифр на 15 элементов. На вход 
#  подаётся трёхзначное натуральное число. Напишите программу, 
#  которая определяет, есть в массиве последовательность из 
#  трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

def array_to_string_of_numbers(array):
    string = str(array)
    string = string.replace(',', '')
    string = string.replace(' ', '')
    return string

size = 15
array = [random.randint(0, 9) for i in range(size)]
string = array_to_string_of_numbers(array)
substring = str(random.randint(100, 999))
print(f'{array} - {substring} -> ', end='')
print('YES' if substring in string else 'NO')