# Напишите программу, которая принимает на вход число
# N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [1, 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Factorial_table(N):
    res = [1]
    fact = 1
    for i in range(1, N + 1):
        fact *= i
        res.append(fact)
    return res

n = int(input('Введите число N: '))
print(f'N = {n} => {Factorial_table(n)}')