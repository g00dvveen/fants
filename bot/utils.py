from telegram import ReplyKeyboardMarkup


def get_keyboard():
    keyboard = ReplyKeyboardMarkup([['Начать']], resize_keyboard=True)
    return keyboard
