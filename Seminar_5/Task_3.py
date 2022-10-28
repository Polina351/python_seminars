# Задайте список случайных чисел от 1 до 10. Посчитайте, 
# сколько всего совпадающих элементов есть в списке. Удалите 
# все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random


def count_double(numbers):
    count = 0
    for i in numbers:
        if numbers.count(i) > 1:
            count += 1
    return count

def list_unical_elements(numbers):
    numbers = set(numbers)
    numbers = list(numbers)
    return numbers


numbers = [random.randint(1, 10) for i in range(10)]   
print(numbers)
print(f'{count_double(numbers)} элемента(ов) совпадают')
print(f'Список уникальных элементов {list_unical_elements(numbers)}')