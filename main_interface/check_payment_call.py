from aiogram import Dispatcher, types
from classes.MainClasses import User, Payment
from classes.Invoice import MyInvoice
from database.run_db import user_tb, payment_tb
from texts import texts
from keyboards import after_pay_keyboard
from config import SUBSCRIPTION_PRICE
from run_bot import bot


async def payment_status_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    my_invoice = MyInvoice.find_create_invoice_object(call.data.split("-")[1])

    if await my_invoice.check_invoice(call.data.split("-")[2]):
        payment_db = Payment(payment_tb)
        await payment_db.add_payment(
            user_id=call.from_user.id,
            currency=my_invoice.currency,
            payment_method=my_invoice.method_name,
            amount=my_invoice.amount,
            amount_usd=SUBSCRIPTION_PRICE,
            parameter=call.data.split("-")[2]
        )
        await call.message.delete()
        await bot.send_message(user.user_id, texts[user.language]["successfully_paid"],
                               reply_markup=after_pay_keyboard(user.language))
        await user.make_subscriber()
    else:
        await call.answer(text=texts[user.language]["not_paid"])


def register_check_payment_call(dp: Dispatcher):
    dp.register_callback_query_handler(payment_status_callback,
                                       lambda call: call.data.split("-")[0] == "check_payment")
