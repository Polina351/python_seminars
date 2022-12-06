# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость 
# квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости 
# квадратного метра каждого дома и список 
# подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади 
# от 100 до 300 кв. метров, цены от 3 до 20 млн

import random
import matplotlib.pyplot as plt

size = 15
S = [random.randint(100, 300) for i in range(size)]
price = [random.randint(3, 20) for i in range(size)]
print(f'Площадь домов:{S}')
print(f'Цена, млн руб:{price}')

cost_for_meter = []
for i in range(size):
    cost_for_meter.append(round((price[i]*1000 )/ S[i],2))
print('Цена за метр:')
print(cost_for_meter)

find_hauses = {}
for i in range(size):
    if cost_for_meter[i] < 50:
        find_hauses[i] = cost_for_meter[i]

sorted_hauses = dict(sorted(find_hauses.items(), key=lambda item: item[1]))


print('Список подходящих домов {№дома по списку : цена за кв}')
print(sorted_hauses)

plt.plot(cost_for_meter)
plt.show()