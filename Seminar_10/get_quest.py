import telebot

bot = telebot.TeleBot("TOKEN", parse_mode= None)

@bot.message_handler(content_types=["text"])
def get_question(message):
  data = open('user_questions.txt', 'a+', encoding='utf-8')
  data.writelines(f'{message.from_user.id}:{message.from_user.first_name}:{message.text} \n')
  data.close()

bot.infinity_polling()