# Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму 
# главной диагонали матрицы.

import random


def get_matrix(matrix, size):
    for i in range(size):
        matrix[i] = list(0 for _ in range(size))
    return matrix

def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(1, 9)
    return matrix

def sum_main_diagonal(matrix, size):
    result = 0
    for i in range(size):
        result += matrix[i][i]
    return result
    
def print_matrix(matrix):
    for row in matrix:
        print(row)

def find_rows_with_larger_sum(matrix, size, sum_main_diagonal):
    dictionary = {}
    for i in range(size):
        sum_row = 0
        for j in range(size):
            sum_row += matrix[i] [j]
        if sum_row > sum_main_diagonal:
            dictionary[i + 1] = sum_row
    return dictionary

            
size = random.randint(3, 5)
matrix = [0] * size
matrix = get_matrix(matrix, size)
matrix = fill_matrix(matrix)
print_matrix(matrix)
sum_main_diagonal = sum_main_diagonal(matrix, size)
print(f'Сумма главной диагонали равна {sum_main_diagonal}')
print('Строки, сумма элементов которых превышает сумму главной диагонали\n(строка: значение суммы):')
print(find_rows_with_larger_sum(matrix, size, sum_main_diagonal))