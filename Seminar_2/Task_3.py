# Даны две строки. Посчитайте сколько раз каждый 
# символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def count_simbol_in_string(string_one, string_two):
    for simbol in set(string_one):
        print(f'{simbol} - {string_two.count(simbol)}')


string_one = 'onen'
string_two = 'onetwonine'
count_simbol_in_string(string_one, string_two)