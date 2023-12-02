import uuid
from .base import BaseModel
from .user import User
from peewee import CharField, ForeignKeyField


class File(BaseModel):
    file_id = CharField(max_length=128)
    unique_id = CharField(max_length=128)
    file_type = CharField(max_length=128)
    added_by = ForeignKeyField(User, backref='files')

    def __repr__(self) -> str:
        return f'<File {self.id}>'

    @classmethod
    def create_from_update(cls, update, user):
        if update.message.document:
            file_id = update.message.document.file_id
            file_type = "document"
        elif update.message.video:
            file_id = update.message.video.file_id
            file_type = "video"
        elif update.message.audio:
            file_id = update.message.audio.file_id
            file_type = "audio"
        elif update.message.photo:
            file_id = update.message.photo[-1].file_id
            file_type = "photo"
        elif update.message.video_note:
            file_id = update.message.video_note.file_id
            file_type = "video_note"
        elif update.message.animation:
            file_id = update.message.animation.file_id
            file_type = "animation"
        elif update.message.sticker:
            file_id = update.message.sticker.file_id
            file_type = "sticker"
        elif update.message.voice:
            file_id = update.message.voice.file_id
            file_type = "voice"
        else:
            return None

        unique_id = "f" + str(uuid.uuid4())

        file = cls(
            file_id=file_id,
            unique_id=unique_id,
            file_type=file_type,
            added_by=user
        )
        file.save(force_insert=True)

        return file

    def get_link(self, bot_username=None):
        return f"https://t.me/{bot_username}?start={self.unique_id}"

    class Meta:
        table_name = 'files'
