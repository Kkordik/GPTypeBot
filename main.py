import asyncio
from run_bot import dp
from main_interface.start_cmd import register_main_start_cmd
from inline_interface.inline_query import register_inline_query_handler
from main_interface.guide_call import register_guide_call


async def main(_loop):
    register_main_start_cmd(dp)
    register_inline_query_handler(dp)
    register_guide_call(dp)
    await dp.start_polling()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
