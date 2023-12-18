from dotenv import load_dotenv
import os


load_dotenv()
BOT_CATCHING_TELEGRAM_API = os.getenv("BOT_CATCHING_TELEGRAM_API")
USER_TELEGRAM_ID = os.getenv("USER_TELEGRAM_ID")
TELEGRAM_ON = os.getenv("TELEGRAM_ON")
