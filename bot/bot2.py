from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import ConversationHandler

import env
import handlers


def main():
    bot = Updater(env.token)
    bot.dispatcher.add_handler(CommandHandler('start', handlers.start))
    # bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать игру'), handlers.start_game))
    bot.dispatcher.add_handler(ConversationHandler(entry_points=[MessageHandler(Filters.regex('Поехали'), handlers.registration)],
                                                   states={
                                                       'user_name': [MessageHandler(Filters.text, handlers.get_user_name)],
                                                       'user_sex': [MessageHandler(Filters.text, handlers.get_user_sex)],
                                                       'partner_name': [
                                                           MessageHandler(Filters.text, handlers.get_partner_name)],
                                                   },
                                                   fallbacks=[]))
    bot.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Начать игру'), handlers.start_game)],
                            states={
                                'show_task': [MessageHandler(Filters.text, handlers.show_task)],
                                'next_task': [MessageHandler(Filters.regex('Следующее задание'), handlers.next_task)],
                                'partner_name': [
                                    MessageHandler(Filters.text, handlers.get_partner_name)],
                            },
                            fallbacks=[]))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, handlers.parrot))
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
