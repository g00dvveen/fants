from telegram import ReplyKeyboardMarkup


def get_keyboard():
    keyboard = ReplyKeyboardMarkup([['Начать игру']], resize_keyboard=True)
    return keyboard
