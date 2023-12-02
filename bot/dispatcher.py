from telegram.ext import Dispatcher
from telegram.ext import CommandHandler, MessageHandler, Filters
from bot.handlers import user
from bot.handlers import admin


def setup_dispatcher(dispatcher: Dispatcher):
    dispatcher.add_handler(CommandHandler('start', user.command_start))
    dispatcher.add_handler(CommandHandler('admin', admin.command_admin))
    dispatcher.add_handler(CommandHandler('format', user.command_format))
    dispatcher.add_handler(MessageHandler(
        Filters.document | Filters.video | Filters.audio |
        Filters.photo | Filters.video_note | Filters.animation |
        Filters.sticker | Filters.voice, user.get_file))

    return dispatcher
