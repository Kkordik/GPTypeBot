from aiogram import Dispatcher, types
from aiogram.types.message import ContentTypes
from GPTBot.classes.MainClasses import User, Payment
from GPTBot.classes.Invoice import CardInvoice, MyInvoice
from GPTBot.database.run_db import user_tb, payment_tb
from GPTBot.texts import texts
from GPTBot.keyboards import after_pay_keyboard
from GPTBot.config import SUBSCRIPTION_PRICE
from GPTBot.run_bot import bot


async def pre_checkout_update(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout.id, ok=True)


async def successful_payment_msg(message: types.Message):
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()

    payment_db = Payment(payment_tb)
    await payment_db.add_payment(
        user_id=message.from_user.id,
        currency=message.successful_payment.currency,
        payment_method=CardInvoice.method_name,
        amount=message.successful_payment.total_amount / 100,
        amount_usd=SUBSCRIPTION_PRICE,
        parameter=message.successful_payment.invoice_payload
    )
    await bot.send_message(user.user_id, texts[user.language]["successfully_paid"],
                           reply_markup=after_pay_keyboard(user.language))
    await user.make_subscriber()
    await MyInvoice.notify_admin_successful_pay(
        bot=bot,
        pay_parameter=message.successful_payment.invoice_payload,
        user=message.from_user,
        amount=message.successful_payment.total_amount / 100,
        currency=message.successful_payment.currency
    )


def register_successful_payment_msg(dp: Dispatcher):
    dp.register_message_handler(successful_payment_msg, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_pre_checkout_query_handler(pre_checkout_update, lambda pre_checkout: True)
