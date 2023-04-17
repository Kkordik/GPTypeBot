import asyncio
from aiogram import Dispatcher, types
from classes.MainClasses import User, Payment
from classes.Invoice import MyInvoice
from database.run_db import user_tb, payment_tb
from texts import texts
from keyboards import payment_url_keyboard, after_pay_keyboard
from config import PAY_WAIT_TIME, PAY_CHECK_INTERVAL, SUBSCRIPTION_PRICE
from run_bot import bot


async def payment_currency_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    if not await user.check_subscription():

        my_invoice = MyInvoice.find_create_invoice_object(call.data.split("-")[1])

        my_invoice.currency = call.data.split("-")[2]
        my_invoice.amount = my_invoice.calculate_price(chosen_currency=my_invoice.currency)

        pay_url = await my_invoice.create_invoice_url()
        keyboard = payment_url_keyboard(
            lang=user.language,
            pay_url=pay_url,
            payment_method=my_invoice.method_name,
            parameter=my_invoice.get_invoice_parameter()
        )

        pay_msg = await call.message.edit_text(text=texts[user.language][my_invoice.invoice_text_name],
                                               reply_markup=keyboard)

        for _ in range(int(PAY_WAIT_TIME / PAY_CHECK_INTERVAL)):
            if await my_invoice.check_invoice():
                payment_db = Payment(payment_tb)
                await payment_db.add_payment(
                    user_id=call.from_user.id,
                    currency=my_invoice.currency,
                    payment_method=my_invoice.method_name,
                    amount=my_invoice.amount,
                    amount_usd=SUBSCRIPTION_PRICE,
                    parameter=my_invoice.get_invoice_parameter()
                )
                await pay_msg.delete()
                await bot.send_message(user.user_id, texts[user.language]["successfully_paid"],
                                       reply_markup=after_pay_keyboard(user.language))
                await user.make_subscriber()
                break
            else:
                await asyncio.sleep(PAY_CHECK_INTERVAL)

    else:
        await call.message.edit_text(text=texts[user.language]["already_premium"], reply_markup=None)


def register_payment_currency_call(dp: Dispatcher):
    dp.register_callback_query_handler(payment_currency_callback,
                                       lambda call: call.data.split("-")[0] == "payment_currency")
