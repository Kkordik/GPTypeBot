import asyncio
from GPTypeBot.run_bot import dp
from GPTypeBot.main_interface.start_cmd import register_main_start_cmd
from GPTypeBot.inline_interface.inline_query import register_inline_query_handler
from GPTypeBot.inline_interface.inline_feedback import register_inline_feedback_handler
from GPTypeBot.main_interface.guide_call import register_guide_call
from GPTypeBot.main_interface.message_query import register_message_query_cmd
from GPTypeBot.main_interface.context_call import register_context_call
from GPTypeBot.main_interface.create_topic_call import register_new_topic_call
from GPTypeBot.main_interface.choose_topic_call import register_choose_topic_call
from GPTypeBot.main_interface.cancel_state import register_cancel_state
from GPTypeBot.main_interface.return_inline_call import register_return_inline_call
from GPTypeBot.main_interface.premium_call import register_premium_call
from GPTypeBot.main_interface.payment_method_call import register_payment_method_call
from GPTypeBot.main_interface.payment_currency_call import register_payment_currency_call
from GPTypeBot.main_interface.check_payment_call import register_check_payment_call
from GPTypeBot.main_interface.successfull_pay_msg import register_successful_payment_msg
from GPTypeBot.main_interface.oferta_cmd import register_oferta_cmd


async def main(_loop):
    register_main_start_cmd(dp)
    register_inline_query_handler(dp)
    register_guide_call(dp)
    register_message_query_cmd(dp)
    register_inline_feedback_handler(dp)
    register_context_call(dp)
    register_new_topic_call(dp)
    register_choose_topic_call(dp)
    register_cancel_state(dp)
    register_return_inline_call(dp)
    register_premium_call(dp)
    register_payment_method_call(dp)
    register_payment_currency_call(dp)
    register_check_payment_call(dp)
    register_successful_payment_msg(dp)
    register_oferta_cmd(dp)
    await dp.start_polling()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
