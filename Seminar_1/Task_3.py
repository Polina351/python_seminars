# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def Range_coordinate_system(number):
    if number == 1:
        return 'I (X > 0, Y > 0)'
    elif number == 2:
        return 'II (X < 0, Y > 0)'
    elif number == 3:
        return 'III (X < 0, Y < 0)'
    elif number == 4:
        return 'IV (X > 0, Y < 0)'


number = (int(input('Введите номер четверти: ')))
if 0 < number < 5:
    print(Range_coordinate_system(number))
else:
    print('Неверное значение!')