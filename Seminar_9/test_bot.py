import telebot
import requests
import time
from random import randint

number = None
is_started = False
is_formula = False
formula = None

bot = telebot.TeleBot("TOKEN", parse_mode= None)

@bot.message_handler(content_types=["text"])
def hello_user(message):
    global number
    global is_started
    global user_number
    global formula
    global is_formula

    if is_formula:
        formula = message.text
        bot.send_message(message.chat.id, f'{formula} = {eval(formula)}')
        is_formula = False
    elif is_started:
        if message.text.isdigit():
            user_number = int(message.text)
            if user_number > number:
                bot.send_message(message.chat.id, 'Меньше')
            elif user_number < number:
                bot.send_message(message.chat.id, 'Больше')
            elif user_number == number:
                bot.send_message(message.chat.id, f'Угадал! Я загадал число {number}')
                is_started = False
        else:
            bot.send_message(message.chat.id, 'Введите число от 1 до 1000')
    else:
        if 'привет' in message.text:
            bot.reply_to(message, 'Привет, ' + message.from_user.first_name)
        elif message.text == 'играть':
            number = randint(1,1000)
            is_started = True
            bot.send_message(message.chat.id, 'Угадай число от 1 до 1000, которое я загадал')
        elif message.text == 'погода':
            r = requests.get('https://wttr.in/?0T')
            bot.reply_to(message, r.text)
        elif message.text == 'котик':
            r = f'https://cataas.com/cat?t=${time.time()}'
            bot.send_photo(message.chat.id, r)
        elif message.text == 'файл':
            data = open('fruits.txt', encoding='utf-8')
            bot.send_document(message.chat.id, data )
            data.close()
        elif message.text == 'вычислить':
            is_formula = True
            bot.send_message(message.chat.id, 'Введите выражение')

        data = open('user_message.txt', 'a+', encoding='utf-8')
        data.writelines(f'id: {message.from_user.id}, name: {message.from_user.first_name} text: {message.text} \n')
        data.close()


bot.infinity_polling()