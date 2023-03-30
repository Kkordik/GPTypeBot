from aiogram import Dispatcher, types
from classes.MainClasses import User
from classes.Tip import *
from database.run_db import user_tb
from texts import texts, facts
from keyboards import start_keyboard
from classes.Guide import GuidePage
from run_bot import bot


async def simple_start_cmd(message: types.Message):
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    await user.insert_user()

    if message.text == "/start":
        await message.answer(texts[user.language]['start_text'],
                             parse_mode="HTML",
                             reply_markup=start_keyboard(user.language))
    else:
        param_type = message.text.split(" ")[1].split("-")[0]
        param = message.text.split(" ")[1].split("-")[1]
        if param_type == "tip":
            tip_type: Tip = globals()[param]
            tip: Tip = tip_type(language=user.language)
            await tip.pm_button_reaction(bot=bot, chat_id=message.chat.id, user=message.from_user)


def register_main_start_cmd(dp: Dispatcher):
    dp.register_message_handler(simple_start_cmd, commands=["start"])
