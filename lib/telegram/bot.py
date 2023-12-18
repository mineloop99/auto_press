from datetime import datetime
import telegram

from lib.telegram.config import BOT_CATCHING_TELEGRAM_API, USER_TELEGRAM_ID, TELEGRAM_ON

isSending = False


async def send_message(text: str):
    if TELEGRAM_ON != "True":
        return
    global isSending
    isSending = True
    if BOT_CATCHING_TELEGRAM_API == None:
        print("No bot init! will not send msg!")
        return
    _bot = telegram.Bot(BOT_CATCHING_TELEGRAM_API)
    async with _bot:
        await _bot.send_message(text=text, chat_id=USER_TELEGRAM_ID)
        print("Message sent!")
        isSending = False
