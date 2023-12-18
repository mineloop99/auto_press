from dotenv import load_dotenv
import os


load_dotenv()
EXECUTABLE_TESSERACT_FILE = os.getenv("EXECUTABLE_TESSERACT_FILE")
BOT_CATCHING_TELEGRAM_API = os.getenv("BOT_CATCHING_TELEGRAM_API")
USER_TELEGRAM_ID = os.getenv("USER_TELEGRAM_ID")
