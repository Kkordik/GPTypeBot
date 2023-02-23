from aiogram import Dispatcher, types
from classes.main_classes import User
from database.run_db import user_tb
from texts import texts


async def start_cmd(message: types.Message):
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    await user.insert_user()
    await message.answer(texts[user.language]['start_text'], parse_mode="HTML")


def register_main_start_cmd(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands="start")
