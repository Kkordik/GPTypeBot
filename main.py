import asyncio
from run_bot import dp
from main_interface.start_cmd import register_main_start_cmd
from inline_interface.inline_query import register_inline_query_handler
# from main_interface.temporar import register_get_photo_id


async def main(_loop):
    # Register handlers
    register_main_start_cmd(dp)
    register_inline_query_handler(dp)
    #register_get_photo_id(dp)

    await dp.start_polling()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
