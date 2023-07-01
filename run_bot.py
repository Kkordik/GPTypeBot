from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from GPTBot.config import BOT_TOKEN


if __name__ == "GPTBot.run_bot":
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
