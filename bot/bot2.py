from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

import env
import handlers


def main():
    bot = Updater(env.token, 'https://telegg.ru/orig/bot')
    bot.dispatcher.add_handler(CommandHandler('start', handlers.sms))
    bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), handlers.sms))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, handlers.parrot))
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
