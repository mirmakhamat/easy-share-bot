import os
import dotenv
dotenv.load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None:
    raise Exception('TELEGRAM_TOKEN is not set')

ADMIN_ID = int(os.getenv('ADMIN_ID', 0))

PSQL_HOST = os.getenv('PSQL_HOST', 'localhost')
PSQL_DB = os.getenv('PSQL_DB')
PSQL_USER = os.getenv('PSQL_USER', 'postgres')
PSQL_PASSWORD = os.getenv('PSQL_PASSWORD')
PSQL_PORT = os.getenv('PSQL_PORT', 5432)

SQLITE_DB = os.getenv('SQLITE_DB')

if PSQL_DB is None and SQLITE_DB is None:
    raise Exception('PSQL_DB or SQLITE_DB is not set')
