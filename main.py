import asyncio
from run_bot import dp
from main_interface.start_cmd import register_main_start_cmd
from inline_interface.inline_query import register_inline_query_handler
from inline_interface.inline_feedback import register_inline_feedback_handler
from main_interface.guide_call import register_guide_call
from main_interface.message_query import register_message_query_cmd
from main_interface.context_call import register_context_call
from main_interface.create_topic_call import register_new_topic_call
from main_interface.choose_topic_call import register_choose_topic_call
from main_interface.cancel_state import register_cancel_state
from main_interface.return_inline_call import register_return_inline_call
from main_interface.premium_call import register_premium_call
from main_interface.payment_method_call import register_payment_method_call
from main_interface.payment_currency_call import register_payment_currency_call
from main_interface.check_payment_call import register_check_payment_call


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
    await dp.start_polling()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
