from .base import BaseModel
from peewee import CharField, ForeignKeyField, BooleanField


class User(BaseModel):
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128, null=True)
    username = CharField(max_length=64, null=True)
    added_by = ForeignKeyField('self', backref='refs', null=True)
    is_admin = BooleanField(default=False)

    def create_from_update_and_context(cls, update, context):
        user = update.effective_user

        defaults = {
            'first_name': user.first_name,
        }

        if user.username:
            defaults['username'] = user.username
        if user.last_name:
            defaults['last_name'] = user.last_name
        if context.args and context.args[0].startswith("r"):
            added_by_id = int(context.args[0].split("r")[1])
            added_by = cls.get_or_none(id=added_by_id)
            if added_by and added_by.id != user.id:
                defaults['added_by'] = added_by

        user, _ = cls.get_or_create(
            id=update.message.from_user.id,
            defaults=defaults
        )
        return user

    def __repr__(self) -> str:
        return f'<User {self.username or self.id}>'

    class Meta:
        table_name = 'users'
