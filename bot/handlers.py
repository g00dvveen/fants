import utils
from telegram import ReplyKeyboardRemove
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

import env
import users
import tasks


user = None
tasks = tasks.get_tasks()


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
    bot.message.reply_text('Игра начинается',  reply_markup=utils.get_keyboard())
    return ConversationHandler.END


def start_game(bot, update):
    global user
    replay_keyboard = [['Зеленый', 'Желтый', 'Красный']]
    bot.message.reply_text(
        'Выбери уровень:',
        reply_markup=ReplyKeyboardMarkup(replay_keyboard, resize_keyboard=True, one_time_keyboard=True))
    return 'show_task'


def show_task(bot, update):
    global user
    user.current_task = 0
    user.level = bot.message.text
    replay_keyboard = [['Следующее задание']]
    task = tasks[user.current_task]
    if task.image is not None:
        update.bot.sendAnimation(
            chat_id=bot.message.chat.id,
            animation=open('../../img/tasks/'+task.image, 'rb'),
            caption=task.description,
            reply_markup=ReplyKeyboardMarkup(replay_keyboard, resize_keyboard=True, one_time_keyboard=True))
    else:
        bot.message.reply_text(
            task.description,
            reply_markup=ReplyKeyboardMarkup(replay_keyboard, resize_keyboard=True, one_time_keyboard=True))
    return 'next_task'

def next_task(bot, update):
    global user
    user.current_task += 1
    replay_keyboard = [['Следующее задание']]
    if user.current_task < len(tasks):
        task = tasks[user.current_task]
        if task.image is not None:
            update.bot.sendAnimation(
                chat_id=bot.message.chat.id,
                animation=open('../../img/tasks/' + task.image, 'rb'),
                caption=task.description,
                reply_markup=ReplyKeyboardMarkup(replay_keyboard, resize_keyboard=True, one_time_keyboard=True))
        else:
            bot.message.reply_text(
                task.description,
                reply_markup=ReplyKeyboardMarkup(replay_keyboard, resize_keyboard=True, one_time_keyboard=True))
        return 'next_task'
    else:
        bot.message.reply_text('Фанты закончились', reply_markup=utils.get_keyboard())
        return ConversationHandler.END
