import utils


def sms(bot, update):
    print('Command start has been sent')
    bot.message.reply_text('Привет, '+format(bot.message.chat.first_name)+'!', reply_markup=utils.get_keyboard())


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)