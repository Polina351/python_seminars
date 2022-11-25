# В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с 
# наилучшим средним баллом.

import random

def get_matrix(matrix):
    for i in range(len(matrix)):
        matrix[i] =  list (0 for _ in range(random.randint(20, 30)))
    return matrix

def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i] [j] = random.randint(3, 5)
    return matrix

def score_average_of_group(matrix):
    dictionary = {}
    for i in range(len(matrix)):
        sum_score = 0
        for j in range(len(matrix[i])):
            sum_score += matrix[i] [j]
        dictionary[i + 1] = round(sum_score / len(matrix[i]), 2)
    return dictionary  

def print_matrix(matrix):
    for row in matrix: 
        print(row)


groups = random.randint(4, 7)
matrix = [0] * groups

matrix = get_matrix(matrix)
fill_matrix(matrix)
print_matrix(matrix)
dictionary = score_average_of_group(matrix)
print(f'Средний балл каждой группы {dictionary}')

print(f'Наилучший средний балл у группы {max(dictionary, key = dictionary.get)}')