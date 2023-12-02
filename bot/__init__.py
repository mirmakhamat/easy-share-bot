from telegram.ext import Updater
from settings import TELEGRAM_TOKEN
from bot.dispatcher import setup_dispatcher


def run():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    setup_dispatcher(dispatcher)

    updater.start_polling()
    updater.idle()
