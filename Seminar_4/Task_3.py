# Выведите число π с заданной точностью. Точность 
# вводится пользователем в виде натурального числа.
# 3 -> 3.142
# 5 -> 3.14159
import math

n = int(input('Задайте точность: '))
print(f'{n} -> {round(math.pi, n)}')