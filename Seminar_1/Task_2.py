# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между
# ними в 2D пространстве.
# A (3,6); B (2,1)    -> 5,1
# A (7,-5); B (1,-1)  -> 7,21

from cmath import sqrt


def Vector(x1, x2, y1, y2):
    res = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return res


x1 = int(input('Введите значение X1: '))
x2 = int(input('Введите значение X2: '))
y1 = int(input('Введите значение Y1: '))
y2 = int(input('Введите значение Y2: '))
vect = float(Vector(x1, x2, y1, y2).real)

print(f'A({x1},{y1}); B({y1},{y2})=> {vect:.2f}')
