from aiogram import Dispatcher, types
from classes.Guide import GuidePage
from classes.MainClasses import User
from database.run_db import user_tb
from run_bot import bot


async def guide_callback(call: types.CallbackQuery):
    page_name = call.data.split("-")[1]
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()
    guide_page = GuidePage(language=user.language, text_name=page_name)
    await guide_page.send_page(bot=bot, chat_id=call.message.chat.id, message=call.message)


def register_guide_call(dp: Dispatcher):
    dp.register_callback_query_handler(guide_callback, lambda call: call.data.split("-")[0] == "guide")
