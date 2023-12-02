from i18n.translator import t
from telegram import Update
from telegram.ext import CallbackContext
from utils.decorators import admin_required


@admin_required
def command_admin(update: Update, context: CallbackContext):
    user = update.message.from_user

    update.message.reply_text(t('admin-message', name=user.first_name))
