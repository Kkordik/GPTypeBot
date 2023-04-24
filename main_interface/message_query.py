import asyncio
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
from classes.Tip import MsgAnswerMistake, WaitAskLater
import hashlib
import random
import string
from config import USER_ROLE, BOT_ROLE, WAIT_TIME, MISTAKE_WAIT_TIME


# A dict for users that sent a message query less than 30s (or other timeout time (see config)) ago.
waiting_dict = {}  # {user_id: <datetime_query>}


async def message_query(message: types.Message):
    print("entered other")
    time_st = time()
    # Returning if message sent by bot (any inline bot or in a group)
    if message.via_bot:
        return

    # Inserting user to db and getting user's language
    user_db = User(
        user_tb,
        message.from_user.id,
        user=message.from_user
    )
    await user_db.get_language()
    await user_db.insert_user()

    # Sending wait message to show that bot received the query
    waiting_msg = await message.answer(text=texts[user_db.language]["getting_query_ready"])

    rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    result_id: str = hashlib.md5(message.text.encode()).hexdigest() + rand_str

    try:
        # Dividing query into sub-queries or if only one query - getting it as a sub-query.
        # And replacing sub-queries in answer text with {} to make possible later add answers at the same places
        query_t = Query(
            language=user_db.language,
            text=message.text,
            from_user=message.from_user,
            short_answers=False
        )
        mistake, _ = query_t.divide_query(query_t.get_markers_list())

        # Returning mistake marker if while dividing query found wrong markers usage
        if mistake:
            return await mistake.send_message_tip(waiting_msg)

        # Sending a waiting tip if user is in a waiting dict and asked query less than waiting_time(see config) ago
        now_time = time()
        if message.from_user.id in waiting_dict:
            next_query_time = waiting_dict[message.from_user.id]

            if now_time < next_query_time:
                left_time = int(next_query_time - now_time)
            else:
                left_time = 0
                del waiting_dict[message.from_user.id]

            return await WaitAskLater(user_db.language, left_time).send_message_tip(waiting_msg)

        else:
            waiting_dict[message.from_user.id] = now_time + WAIT_TIME  # Adding user to the waiting dict if he wasn't

        # Adding previous messages to the query based on the user's current chosen topic.
        # If topic_id is 0 than no history is taken
        topic_id = await user_db.get_current_topic_id()
        query_db = QueryDb(query_tb)
        prev_queries_db = await query_db.get_previous_queries(topic_id=topic_id)
        query_t.prev_messages.add_previous_queries(prev_queries_db)

        # Editing the wait message to show that bot is waiting for the openai answers
        await waiting_msg.edit_text(text=texts[user_db.language]["waiting_for_openai"])

        # Receiving answers to the sub-queries
        answers = await query_t.answer_sub_queries()
        query_t.answer = query_t.answer.format(*answers)  # Replacing {} with answers in the answer text

        # Deleting waiting message and sending an answer (not editing because of lack of a notification)
        await waiting_msg.delete()
        waiting_msg = await bot.send_message(
            chat_id=message.chat.id,
            text=query_t.answer,
            disable_web_page_preview=True
        )

        # Delete all unsent messages from the database (only to free the memory because
        # such messages aren't taken to the context)
        await query_db.delete_all_unsent(user_id=message.from_user.id)

        # Adding sub-queries to the database and setting as sent
        for sub_query_id, sub_query in enumerate(query_t.sub_queries):
            await query_db.insert_query(
                result_id=result_id,
                subquery_id=sub_query_id,
                orig_query=query_t.text,
                query=sub_query.text,
                answer=sub_query.answer,
                topic_id=topic_id,
                user_id=user_db.user_id
            )
        await query_db.set_as_sent(result_id=result_id)

        program_time = time() - time_st

        # Waiting the wait_time minus time spent by the program
        await asyncio.sleep(WAIT_TIME - program_time)

    except Exception as ex:
        await MsgAnswerMistake(language=user_db.language).send_message_tip(waiting_msg)
        print(datetime.datetime.now(), ex, sep="  msg  ")

        waiting_dict[message.from_user.id] = time() + MISTAKE_WAIT_TIME  # Editing next query time in waiting dict
        # Waiting mistake wait time (less that wait time) to make asking query again faster
        await asyncio.sleep(MISTAKE_WAIT_TIME)

    # Deleting the user from waiting dict after he waited the waiting time
    del waiting_dict[message.from_user.id]


def register_message_query_cmd(dp: Dispatcher):
    dp.register_message_handler(message_query,
                                lambda message: not message.successful_payment and message.content_type == "text")
