from peewee import Model, BigIntegerField, DateTimeField
from datetime import datetime
from db.loader import database


class BaseModel(Model):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
