# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Сдвиньте все элементы списка на 2
# позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def Get_list(N):
    N = abs(N)
    res_list = []
    for i in range(-N, N+1):
        res_list.append(i)
    return res_list


def Move_Steps_to_the_left(list, step):
    new_list = list[-step:] + list[:-step]
    return new_list


N = int(input('Введите число N: '))
list = Get_list(N)
step = 2
new_list = Move_Steps_to_the_left(list, step)
print(f'{N} => {new_list}')