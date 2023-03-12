from aiogram import Dispatcher, types
from classes.MainClasses import User
from database.run_db import user_tb
from texts import texts, facts
from keyboards import start_keyboard
from classes.Guide import GuidePage
from run_bot import bot
from time import time
from classes.Query import Query


async def message_query(message: types.Message):
    if message.via_bot:
        return
    
    time_st = time()
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    await user.insert_user()
    waiting_msg = await message.answer(text=texts[user.language]["wait_for_answer"])

    query_t = Query(language=user.language, text=message.text, from_user=message.from_user, short_answers=False)
    mistake = query_t.divide_query(query_t.get_markers_list())

    if not mistake:
        time_f = time()
        answers = await query_t.answer_sub_queries()
        query_t.answer = query_t.answer.format(*answers)
        print(time_f-time_st)
        await waiting_msg.edit_text(text=query_t.answer)

    else:
        await mistake.send_message_tip(waiting_msg)


def register_message_query_cmd(dp: Dispatcher):
    dp.register_message_handler(message_query, content_types=["text"])
