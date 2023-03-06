from aiogram import Dispatcher, types


async def guide_callback(call: types.CallbackQuery):
    await call.answer(text="We are working on it🛠")


def register_guide_call(dp: Dispatcher):
    dp.register_callback_query_handler(guide_callback, lambda call: call.data == "guide_but")
