import telebot

bot = telebot.TeleBot("TOKEN", parse_mode= None)
data = open('user_questions.txt', 'r+', encoding='utf-8')
lines = data.readlines()
data.close()
print(lines)

for line in lines:
  print(line)
  if line != '':
    line = line.split(':')
    answer = input(f'Вопрос от {line[1]} \n {line[2]} \n Введите ответ:')
    bot.send_message(line[0], f'Здравствуйте{line[1]}. Ответ на ваш вопрос \n {line[2]} \n Ответ: {answer}')