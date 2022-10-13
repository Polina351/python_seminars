# Напишите программу, которая на вход принимает число (N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def Even_numbers_from_1_to_N(N):
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(i, end=' ')


N = int(input('Введите значение N: '))
if N > 1:
    Even_numbers_from_1_to_N(N)
else:
    print('Чисел нет!')