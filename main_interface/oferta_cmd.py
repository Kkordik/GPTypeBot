from aiogram import Dispatcher, types
from classes.MainClasses import User
from database.run_db import user_tb
from texts import texts
from run_bot import bot
from config import OFERTA_FILE_ID


async def file_message(message: types.Message):
    print("file_id = ", message.document.file_id)


async def simple_oferta_cmd(message: types.Message):
    user_db = User(user_tb, message.from_user.id, user=message.from_user)
    await user_db.get_language()
    await user_db.insert_user()

    await bot.send_document(chat_id=message.chat.id,
                            document=OFERTA_FILE_ID,
                            caption=texts[user_db.language]["oferta_msg"])


def register_oferta_cmd(dp: Dispatcher):
    dp.register_message_handler(simple_oferta_cmd, commands=["oferta"])
    dp.register_message_handler(file_message, content_types=["document"])
