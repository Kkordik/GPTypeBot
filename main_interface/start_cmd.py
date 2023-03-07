from aiogram import Dispatcher, types
from classes.MainClasses import User
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
        guide_page = GuidePage(language=user.language, text_name=message.text.split(" ")[1])
        await guide_page.send_page(bot=bot, chat_id=message.chat.id)


def register_main_start_cmd(dp: Dispatcher):
    dp.register_message_handler(simple_start_cmd, commands=["start"])
