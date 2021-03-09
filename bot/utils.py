from telegram import ReplyKeyboardMarkup


def get_keyboard():
    keyboard = ReplyKeyboardMarkup([['Начать'], ['Заполнить анкету']], resize_keyboard=True)
    return keyboard
