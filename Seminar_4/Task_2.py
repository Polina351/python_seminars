# В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. Выведите 
# названия того товара, который закончился.

# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

data = open('ice_cream.txt', encoding= 'utf-8')
icecream = data.readlines()
data.close()


full_list = set(icecream[0].replace('\n', '').split(', '))
have_list = set(icecream[1].replace('\n', '').split(', '))

print(f'Закончилось: {full_list.difference(have_list)}')
