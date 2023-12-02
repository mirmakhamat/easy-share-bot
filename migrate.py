from peewee_migrate import Router
from db.loader import database

router = Router(database, ignore=['basemodel'])

router.create(auto=['db'])

router.run()
