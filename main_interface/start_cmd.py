from aiogram import Dispatcher, types
from classes.MainClasses import User
from database.run_db import user_tb
from texts import texts, facts, facts_desc


async def simple_start_cmd(message: types.Message):
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    await user.insert_user()
    await message.answer(texts[user.language]['start_text'], parse_mode="HTML")


async def parameter_start_cmd(message: types.Message):
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    await user.insert_user()
    await message.answer(facts_desc[user.language][message.text.split(" ")[1]], parse_mode="HTML")


def register_main_start_cmd(dp: Dispatcher):
    dp.register_message_handler(simple_start_cmd, lambda message: message.text == "/start")
    dp.register_message_handler(parameter_start_cmd, lambda message: message.text != "/start" and "/start" in message.text)
