import asyncio
from aiogram import Dispatcher, types
from classes.MainClasses import User
from database.run_db import user_tb
from keyboards import return_inline_keyboard


async def return_inline_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()
    await call.message.edit_reply_markup(reply_markup=return_inline_keyboard(user.language))
    await asyncio.sleep(3)
    await call.message.edit_reply_markup(reply_markup=None)


def register_return_inline_call(dp: Dispatcher):
    dp.register_callback_query_handler(return_inline_callback, lambda call: call.data.split("-")[0] == "return_inline")
