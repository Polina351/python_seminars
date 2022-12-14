# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

dictionary = \
    {
        'Привет!': 'Приветствую Вас!',
        'Как тебя зовут?': 'Меня зовут Алекс',
        'Какой сегодня день?': 'Чудесный',
        'Пока!': 'Всего доброго!',
        'Выход': 'Всего доброго!'
    }


def work_bot():
    work = True
    while work:
        phrase = input('Я: ')
        if phrase == 'Пока!' or phrase == 'Выход':
            work = False
        if phrase in dictionary.keys():
            print('Бот:', dictionary[phrase])
        else:
            print('Бот: Я слишком глуп,я Вас не понимаю')


work_bot()
