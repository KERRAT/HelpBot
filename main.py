import telebot
import json
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

r1 = "Домашнє насилля"
r2 = "Корупція"
r3 = "Психологічні проблеми"
r4 = "Проблеми доступності"
r5 = "Проблеми зі здоров'ям"
r6 = "Булінг"
r7 = "Насилля"
r8 = "Харасмент"
@bot.message_handler(commands=['start'])
def start(message):
    """
        Создание клавиатуры, отправка пользователю сообщения с клавиатурой
    """
    if message.chat.type == "private":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row(r1, r2)
        keyboard.row(r3, r4)
        keyboard.row(r5, r6)
        keyboard.row(r7, r8)
        keyboard.row("Немає моєї проблеми")
        bot.send_message(message.chat.id, 'Выбирай', reply_markup=keyboard)

    """
        Создание inline клавиатуры и её возврат
    """
def inline_yes_no():
    inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
    InlineButtonYes = types.InlineKeyboardButton(text="Помогло 😊", callback_data="Yes")
    InlineButtonNo = types.InlineKeyboardButton(text="Проблема не рішена 😥", callback_data="No")
    inline_keyboard.row(InlineButtonYes, InlineButtonNo)
    return inline_keyboard

    """
        список, который будет содержать информацию о пользователе
    """
info = list()


@bot.message_handler(content_types=["text"])
def event_button(message):
    """
        добавление пользователя в "активные пользователи" в проблеме
    """
    if message.chat.type == "group":
        if(message.text == "+"):
            try:
                """
                    открытие файла с ид ивентов, загрузка информации из него
                """
                with open("problems.txt") as f:
                    text = f.read()
                    list_ids = json.loads(text)
                    """
                        Проверка есть ли пользователь в списке "на выполнение". Если нету -- добавить
                    """
                if message.reply_to_message.message_id in list_ids:

                    text = message.reply_to_message.text
                    if not '''{}'''.format(message.from_user.first_name) in text:
                        text = message.reply_to_message.text+ '''
                    
{}'''.format(message.from_user.first_name)
                    """
                        Добавление испольнителя для проблемы
                    """
                    bot.edit_message_text(chat_id= message.chat.id,message_id=message.reply_to_message.message_id,text= text)
            except:pass




    if message.chat.type == "private":
        txt = message.text
        if txt == r1:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:11111111111''')


        elif txt == r2:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:2222222222''')
        elif txt == r3:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:333333333''')
        elif txt == r4:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:444444444444''')
        elif txt == r5:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:55555555555''')
        elif txt == r6:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:66666666666''')
        elif txt == r7:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:777777777777''')
        elif txt == r8:
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:88888888888888''')
        elif txt == "9":
            bot.send_message(message.chat.id, '''Ви можете зробити то-то і то-то''', reply_markup=inline_yes_no())

            @bot.callback_query_handler(
                lambda query: query.data == "Yes")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id, '''Ми раді, що ваша проблема рішена 🥰''')

            @bot.callback_query_handler(lambda query: query.data == "No")  # прийом колбеку при натисканні на клавіатуру
            def process_callback(query):
                bot.send_message(query.message.chat.id,
                                 '''Ви можете скористатися найнижньою кнопкою, щоб описати свою проблему або ж позвонити 
    за телефоном:99999999999''')
        elif txt == "Немає моєї проблеми":
            sent = bot.send_message(message.chat.id, "Опишіть Вашу проблему і з чим Ви стикнулись одним повідомленням")
            bot.register_next_step_handler(sent, problem)


def problem(message):
    prob = message.text
    if (prob != "") & (prob != "Немає моєї проблеми"):
        info.append(prob)
        sent = bot.send_message(message.chat.id, "Введіть Ваш номер телефону або ж посилання на любу вашу сторінку, "
                                                 "щоб ми могли з Вами зв'язатися")
        bot.register_next_step_handler(sent, teleph)
    else:
        bot.send_message(message.chat.id,
                         "Невірний опис проблеми. Будь ласка, нажміть кнопку знову та опишіть проблему.")


def teleph(message):
    tel = message.text
    if (tel != "") & (tel != "Немає моєї проблеми"):
        info.append(tel)
    else:
       """" bot.send_message(message.chat.id,
                       "Невірний опис проблеми. Будь ласка, нажміть кнопку знову та опишіть проблему.")"""
    info.append(tel)
    if (info[0] != "") & (info[1] != ""):
        bot.send_message(-359445003, '''Проблема:{}
Телефон:{}'''.format(info[0], info[1]))
        info.clear()
        send = bot.send_message(message.chat.id,
                         "Ваше повідомлення зареєстровано. Очікуйте поки з вами зв'яжуться та нададуть варіанти "
                         "вирішення проблеми")
        list_ids = list()
        with open("problems.txt") as f:
            text = f.read()
            b = json.loads(text)
            for l in b:
                list_ids.append(l)

        with open("problems.txt", "w") as f:
            list_ids.append(send.message_id - 1)
            print(json.dumps(list_ids), file=f)



bot.polling(none_stop=True)
