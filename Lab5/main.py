import telebot

token = "2108013202:AAGE-QbVJ9KqreqSvrayKfETlB2d28N8jAg"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Да', 'Нет')
    bot.send_message(message.chat.id, 'Привет, ты занят?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Отлично! Можешь помочь с элтехом?')
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Жаль, но не мог бы ты помочь с элтехом?')


bot.polling()
