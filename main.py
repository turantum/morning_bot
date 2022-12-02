import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    img = open('logo.jpg', 'rb')

    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Начать", callback_data='go')
    markup.add(btn1)

    mess = f'Письмо от Хэла Элрода, автора книги "Магия утра"\n\n' \
           f'Добро пожаловать в 30-дневную программу преображения! Поздравляю вас — вы набрались ' \
           f'мужества и приняли важное решение встать на путь достижения экстраординарного уровня ' \
           f'жизни. Вы этого заслуживаете.\n\n' \
           f'Первый шаг на пути к личному или профессиональному развитию, как правило, очень трудно' \
           f'сделать, но с этого начинается каждый великий путь. В течение следующих 30 дней вы' \
           f'построите фундамент успеха в каждой области вашей жизни.'
    bot.send_photo(message.chat.id, img, caption=mess, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'go')
def first(call):
    mess = f'<b>ШАГ 1 Давайте немного уточним</b>\n\n' \
           f'Добро пожаловать в 30-дневную программу преображения! Поздравляю вас — вы набрались ' \
           f'мужества и приняли важное решение встать на путь достижения экстраординарного уровня ' \
           f'жизни. Вы этого заслуживаете.\n\n' \
           f'Первый шаг на пути к личному или профессиональному развитию, как правило, очень трудно' \
           f'сделать, но с этого начинается каждый великий путь. В течение следующих 30 дней вы' \
           f'построите фундамент успеха в каждой области вашей жизни.'
    bot.send_photo(call.message.chat.id, caption=mess, parse_mode='html')


bot.polling(none_stop=True)