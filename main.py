from bot import run
from utils.logging import logger
from utils.translations import load_translations

if __name__ == '__main__':
    logger.info("Starting bot")
    load_translations()
    run()
