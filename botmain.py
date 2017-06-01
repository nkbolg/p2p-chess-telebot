import telegram
from bottoken import token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dllusage import askdll

description = \
"""Это бот для игры в шахматы с друзьями через телеграм.
Как играть:
under construction"""


def on_help(bot: telegram.Bot, update: telegram.Update):
    bot.send_message(update.message.chat_id, description)


def on_start(bot: telegram.Bot, update: telegram.Update):
    on_help(bot, update)


def on_text(bot: telegram.Bot, update: telegram.Update):
    cid = update.message.chat_id
    text = update.message.text
    suc, res = askdll(text)
    if not suc:
        bot.send_message(cid, res)
    else:
        bot.send_message(cid, "Valid")


def main():
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, on_text))
    dispatcher.add_handler(CommandHandler('start', on_start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

