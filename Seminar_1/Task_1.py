#  Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и выводит название этого
#  дня недели.
# 1   –> Понедельник
# 10  –> Нет такого дня
# 7   –> Воскресение
def Find_weekday(day):
    if 0 < day <= 7:
        if day == 1:
            return 'Понедельник'
        elif day == 2:
            return 'Вторник'
        elif day == 3:
            return 'Среда'
        elif day == 4:
            return 'Четверг'
        elif day == 5:
            return 'Пятница'
        elif day == 6:
            return 'Суббота'
        elif day == 7:
            return 'Воскресенье'
    else:
        return 'Нет такого дня'


day = int(input('Введите число: '))
print(day, '=>', Find_weekday(day))
