import telebot
from telebot import types

import env
import users
import tasks

bot = telebot.TeleBot(env.token)
user = None

@bot.message_handler(commands=['start'])
def start_message(message):
    global user
    user_id = str(message.from_user.id)
    user = users.get_user(user_id)
    if user.id != '0':
        bot.send_message(user_id, 'Привет, '+user.get_name())
        show_main_menu(user_id)
    else:
        user.id = user_id
        sent = bot.send_message(user_id, 'Давай знакомиться! Как тебя зовут?')
        bot.register_next_step_handler(sent, lambda m: acquaint(m, user_id))


def show_main_menu(user_id):
    markup = generate_main_menu_markup()
    bot.send_message(user_id, text='Начнем игру?', reply_markup=markup)


def generate_main_menu_markup():
    list_items = ['Начать игру', 'Настройки']
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in list_items:
        markup.add(item)
    return markup


def acquaint(message, user_id):
    global user
    user_name = message.text
    user.name = user_name
    sex_keyboard = types.InlineKeyboardMarkup()
    key_male = types.InlineKeyboardButton(text='Мужской', callback_data='set_sex_male')
    sex_keyboard.add(key_male)
    key_female = types.InlineKeyboardButton(text='Женский', callback_data='set_sex_female')
    sex_keyboard.add(key_female)
    bot.send_message(user_id, text='Привет, '+user_name+'!\nТвой пол', reply_markup=sex_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global user
    user_id = str(call.from_user.id)
    if call.data == "set_sex_male":
        user.sex = 'male'
        sent = bot.send_message(user_id, 'Отлично! Как зовут твоего партнера?')
        bot.register_next_step_handler(sent, lambda m: set_partner_name(m, user_id))
    elif call.data == "set_sex_female":
        user.sex = 'female'
        sent = bot.send_message(user_id, 'Отлично! Как зовут твоего партнера?')
        bot.register_next_step_handler(sent, lambda m: set_partner_name(m, user_id))


def set_partner_name(message, user_id):
    global user
    user.partner_name = message.text
    user.save()
    show_main_menu(user_id)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Начать игру":
        start_game(str(message.from_user.id))
    elif message.text == "Настройки":
        show_settings(str(message.from_user.id))
    elif message.text == "Зеленый уровень":
        user.level = 'green'
        user.update(str(message.from_user.id))
        start_tasks(str(message.from_user.id))
    elif message.text == "Желтый уровень":
        user.level = 'yellow'
        user.update(str(message.from_user.id))
        start_tasks(str(message.from_user.id))
    elif message.text == "Красный уровень":
        user.level = 'red'
        user.update(str(message.from_user.id))
        start_tasks(str(message.from_user.id))
    elif message.text == "Главное меню":
        show_main_menu(str(message.from_user.id))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def start_game(user_id):
    global user
    if user.level is None:
        show_levels(user_id)
    else:
        start_tasks(user_id)


def show_levels(user_id):
    markup = generate_levels_markup()
    bot.send_message(user_id, text='Выбери уровень игры', reply_markup=markup)


def generate_levels_markup():
    list_items = ['Зеленый уровень', 'Желтый уровень', 'Красный уровень', 'Главное меню']
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in list_items:
        markup.add(item)
    return markup


def show_settings(user_id):
    markup = generate_settings_markup()
    bot.send_message(user_id, text='Настройки', reply_markup=markup)


def generate_settings_markup():
    list_items = ['Зеленый уровень', 'Желтый уровень', 'Красный уровень', 'Главное меню']
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in list_items:
        markup.add(item)
    return markup


def start_tasks(user_id):
    task_list = tasks.get_tasks()
    markup = next_task_markup()
    bot.send_message(user_id, text=tasks[0].description, reply_markup=markup)


def next_task_markup():
    list_items = ['Следующее задание', 'Следующий уровень', 'Главное меню']
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in list_items:
        markup.add(item)
    return markup


bot.polling(none_stop=True, interval=0)

