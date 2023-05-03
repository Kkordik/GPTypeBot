from aiogram import Dispatcher, types
from classes.MainClasses import User
from database.run_db import user_tb
from run_bot import bot
from texts import texts
from keyboards import payment_method_keyboard


async def premium_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    if not await user.check_subscription():
        keyboard = payment_method_keyboard(user.language)
        await call.message.delete()
        await bot.send_message(chat_id=call.message.chat.id,
                               text=texts[user.language]["premium_benefits"],
                               reply_markup=keyboard)
    else:
        await bot.send_message(call.message.chat.id, text=texts[user.language]["already_premium"])
    await call.answer()


def register_premium_call(dp: Dispatcher):
    dp.register_callback_query_handler(premium_callback, lambda call: call.data == "premium")
