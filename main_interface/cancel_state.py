from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from classes.MainClasses import User
from database.run_db import user_tb
from texts import texts


async def cancel_state_call(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()
    await call.answer(texts[user.language]["canceled"])
    await call.message.delete()


def register_cancel_state(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_state_call, lambda call: call.data == "cancel-state", state='*')
