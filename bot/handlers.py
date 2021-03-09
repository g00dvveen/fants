import utils
from telegram import ReplyKeyboardRemove
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

import env
import users
import tasks


user = None


def start(bot, update):
    global user
    user_id = str(bot.message.chat.id)
    user = users.get_user(user_id)
    if user.id != '0':
        bot.message.reply_text('Привет, '+format(bot.message.chat.first_name)+'!', reply_markup=utils.get_keyboard())
    else:
        user.id = user_id
        replay_keyboard = [['Поехали']]
        bot.message.reply_text(
            'Привет! Давай знакомиться!',
            reply_markup=ReplyKeyboardMarkup(
                replay_keyboard,
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def registration(bot, update):
    bot.message.reply_text('Как тебя зовут?', reply_markup=ReplyKeyboardRemove())
    return 'user_name'


def get_user_name(bot, update):
    global user
    user.name = bot.message.text
    replay_keyboard = [['Мужской', 'Женский']]
    bot.message.reply_text(
        'Укажи свой пол:',
        reply_markup=ReplyKeyboardMarkup(replay_keyboard, resize_keyboard=True, one_time_keyboard=True))
    return 'user_sex'


def get_user_sex(bot, update):
    global user
    if bot.message.text == 'Мужской':
        user.sex = 'male'
    else:
        user.sex = 'female'
    bot.message.reply_text('Как зовут твоего партнера?', reply_markup=ReplyKeyboardRemove())
    return 'partner_name'


def get_partner_name(bot, update):
    global user
    user.partner_name = bot.message.text
    user.save()
    bot.message.reply_text('Игра начинается')
    return ConversationHandler.END
