# В файле находятся названия фруктов. 
# Выведите все фрукты, названия которых 
# начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва

def print_word_by_letter(letter):
    data = open('fruits.txt', encoding='utf-8')
    fruits = data.readlines()
    data.close()
    for fruit in fruits:
        if fruit[0].lower() == letter.lower():
            print(fruit, end='')
        

letter = input('Введите букву: ')
print_word_by_letter(letter)