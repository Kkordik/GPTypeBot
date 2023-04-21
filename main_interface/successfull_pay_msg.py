from aiogram import Dispatcher, types
from classes.MainClasses import User, Payment
from classes.Invoice import CardInvoice
from database.run_db import user_tb, payment_tb
from texts import texts
from keyboards import after_pay_keyboard
from config import SUBSCRIPTION_PRICE
from run_bot import bot


async def successful_payment_message(message: types.Message):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    print(message.from_user.id)

    payment_db = Payment(payment_tb)
    await payment_db.add_payment(
        user_id=message.from_user.id,
        currency=message.successful_payment.currency,
        payment_method=CardInvoice.method_name,
        amount=message.successful_payment.total_amount / 100,
        amount_usd=SUBSCRIPTION_PRICE,
        parameter=message.successful_payment.invoice_payload
    )
    await call.message.delete()
    await bot.send_message(user.user_id, texts[user.language]["successfully_paid"],
                           reply_markup=after_pay_keyboard(user.language))
    await user.make_subscriber()


def register_successful_payment_msg(dp: Dispatcher):
    dp.register_message_handler(successful_payment_message, lambda message: message.successful_payment)
