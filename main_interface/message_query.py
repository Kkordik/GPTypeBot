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
from config import USER_ROLE, BOT_ROLE


async def message_query(message: types.Message):
    time_st = time()
    if message.via_bot:
        return

    user_db = User(user_tb, message.from_user.id, user=message.from_user)
    await user_db.get_language()
    await user_db.insert_user()

    waiting_msg = await message.answer(text=texts[user_db.language]["wait_for_answer"])

    try:
        rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        result_id: str = hashlib.md5(message.text.encode()).hexdigest() + rand_str

        query_t = Query(language=user_db.language, text=message.text, from_user=message.from_user, short_answers=False)
        mistake = query_t.divide_query(query_t.get_markers_list())

        if not mistake:
            if await user_db.check_subscription():
                topic_id = await user_db.get_current_topic_id()
                query_db = QueryDb(query_tb)
                prev_queries_db = await query_db.get_previous_queries(topic_id=topic_id)
                query_t.prev_messages.add_previous_queries(prev_queries_db)

                answers = await query_t.answer_sub_queries()
                query_t.answer = query_t.answer.format(*answers)
                await waiting_msg.edit_text(text=query_t.answer)
                await query_db.delete_all_unsent(user_id=message.from_user.id)

                for sub_query in query_t.sub_queries:
                    await query_db.insert_query(result_id=result_id, query=sub_query.text, answer=sub_query.answer,
                                                topic_id=topic_id, user_id=user_db.user_id)
                    await query_db.set_as_sent(result_id=result_id)

            else:
                answers = await query_t.answer_sub_queries()
                query_t.answer = query_t.answer.format(*answers)
                await waiting_msg.edit_text(text=query_t.answer)

        else:
            await mistake.send_message_tip(waiting_msg)

        print(result_id)

    except Exception as ex:
        print(datetime.datetime.now(), ex, sep="   msg  ")
        await MsgAnswerMistake(language=user_db.language).send_message_tip(waiting_msg)

    time_f = time()
    print(time_f - time_st)


def register_message_query_cmd(dp: Dispatcher):
    dp.register_message_handler(message_query, content_types=["text"])
