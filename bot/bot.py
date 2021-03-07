import env, users
import telebot
from telebot import types


bot = telebot.TeleBot(env.token)

users = users.get_users()

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        bot.send_message(user_id, 'Привет, '+user[user_id])
        show_main_menu(user_id)
    else:
        sent = bot.send_message(user_id, 'Давай знакомиться! Как тебя зовут?')
        bot.register_next_step_handler(sent, lambda m: acquaint(m, user_id))