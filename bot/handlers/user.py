from i18n.translator import t
from telegram import Update
from telegram.ext import CallbackContext
from db.models import User, File


def send_file(update: Update, context: CallbackContext):
    unique_id = context.args[0]
    file = File.get(unique_id=unique_id)

    if file.file_type == 'document':
        update.message.reply_document(file.file_id)
    elif file.file_type == 'video':
        update.message.reply_video(file.file_id)
    elif file.file_type == 'audio':
        update.message.reply_audio(file.file_id)
    elif file.file_type == 'photo':
        update.message.reply_photo(file.file_id)
    elif file.file_type == 'video_note':
        update.message.reply_video_note(file.file_id)
    elif file.file_type == 'animation':
        update.message.reply_animation(file.file_id)
    elif file.file_type == 'sticker':
        update.message.reply_sticker(file.file_id)
    elif file.file_type == 'voice':
        update.message.reply_voice(file.file_id)


def command_start(update: Update, context: CallbackContext):
    user = User.create_from_update_and_context(update, context)

    if context.args and context.args[0].startswith("f"):
        return send_file(update, context)

    update.message.reply_text(t('start-command-message', name=user.first_name))


def command_format(update: Update, context: CallbackContext):
    update.message.reply_text(t('format-command-message'))


def get_file(update: Update, context: CallbackContext):
    user = User.get(id=update.effective_user.id)

    file = File.create_from_update(
        update=update,
        user=user
    )
    if not file:
        return

    update.message.reply_text(
        file.get_link(bot_username=context.bot.username)
    )
