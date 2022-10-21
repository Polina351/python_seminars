#  Создайте файл. Запишите в него N первых элементов 
#  последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def Fibonacci(N):
    num_one = 0
    num_two = 1
    data = open('fibonacci.txt', 'w')
    for i in range(N):
        print(num_one, end=' ')
        data.writelines(str(num_one) + '\n')
        (num_one, num_two) = (num_two, num_one + num_two)

N = int(input('Введите число N: '))
Fibonacci(N)