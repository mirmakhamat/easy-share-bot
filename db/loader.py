from peewee import SqliteDatabase, PostgresqlDatabase
import settings

if settings.PSQL_DB:
    database = PostgresqlDatabase(settings.PSQL_DB, user=settings.PSQL_USER, password=settings.PSQL_PASSWORD,
                                  host=settings.PSQL_HOST, port=settings.PSQL_PORT)
else:
    database = SqliteDatabase(settings.SQLITE_DB)
