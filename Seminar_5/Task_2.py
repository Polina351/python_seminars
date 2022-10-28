# Дан список случайных чисел. Создайте список, в который попадают 
# числа, описывающие возрастающую последовательность. Порядок элементов 
# менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random

list_size = 10
numbers = [random.randint(1, 10) for i in range(list_size)]
print(numbers)

res = []

min = res.append(numbers[0])

for i in range(list_size):
    if res[-1] < numbers[i]:
        res.append(numbers[i])

print(res)