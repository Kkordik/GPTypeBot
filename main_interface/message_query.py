import datetime

from aiogram import Dispatcher, types
from classes.MainClasses import User, QueryDb
from database.run_db import user_tb, query_tb
from texts import texts, facts
from keyboards import start_keyboard
from classes.Guide import GuidePage
from run_bot import bot
from time import time
from classes.Query import Query
from classes.Tip import MsgAnswerMistake
import hashlib
import random
import string


async def message_query(message: types.Message):
    if message.via_bot:
        return

    time_st = time()
    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    await user.insert_user()
    waiting_msg = await message.answer(text=texts[user.language]["wait_for_answer"])

    try:
        query_t = Query(language=user.language, text=message.text, from_user=message.from_user, short_answers=False)
        mistake = query_t.divide_query(query_t.get_markers_list())

        if not mistake:
            rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            result_id: str = hashlib.md5(message.text.encode()).hexdigest() + rand_str

            answers = await query_t.answer_sub_queries()
            query_t.answer = query_t.answer.format(*answers)
            await waiting_msg.edit_text(text=query_t.answer)
            time_f = time()
            print(time_f-time_st)
            print(result_id)

            query_db = QueryDb(query_tb)

            for sub_query in query_t.sub_queries:
                await query_db.insert_query(result_id=result_id, query=sub_query.text, answer=sub_query.answer)
                await query_db.set_as_sent(result_id=result_id)
        else:
            await mistake.send_message_tip(waiting_msg)
    except Exception as ex:
        print(datetime.datetime.now(), ex, sep="     ")
        await MsgAnswerMistake(language=user.language).send_message_tip(waiting_msg)


def register_message_query_cmd(dp: Dispatcher):
    dp.register_message_handler(message_query, content_types=["text"])
