from aiogram import Dispatcher, types
from classes.MainClasses import User
from classes.Invoice import MyInvoice
from database.run_db import user_tb
from texts import texts


async def payment_method_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    if not await user.check_subscription():
        chosen_method_cl = MyInvoice.find_create_invoice_object(call.data.split("-")[1])

        keyboard = await chosen_method_cl.payment_currencies_keyboard(lang=user.language)
        await call.message.edit_text(text=texts[user.language]["premium_benefits"], reply_markup=keyboard)
    else:
        await call.message.edit_text(text=texts[user.language]["already_premium"], reply_markup=None)


def register_payment_method_call(dp: Dispatcher):
    dp.register_callback_query_handler(payment_method_callback, lambda call: call.data.split("-")[0] == "payment_method")
