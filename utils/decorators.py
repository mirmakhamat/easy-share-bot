from functools import wraps
from db.models import User


def admin_required(func):
    @wraps(func)
    def wrapper(update, context, *args, **kwargs):
        user = User.get_or_none(
            id=update.effective_user.id
        )
        if user and user.is_admin:
            return func(update, context, *args, **kwargs)
    return wrapper
