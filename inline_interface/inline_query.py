from aiogram import Dispatcher
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import hashlib
from classes.Query import Query
from texts import texts, facts
from classes.MainClasses import User, QueryDb
from database.run_db import user_tb, query_tb
from classes.Markers import ends_with_marker
from classes.Tip import NoSubscription, StartWithMarker, TooLongQuery, MsgAnswerMistake, EndWithSign, InfoTip
from config import TELEGRAM_CHAR_LIMIT, END_TIP_PROBABILITY
import random
import string
from time import time
from config import BOT_ROLE, USER_ROLE
import datetime


async def inline_echo(inline_query: InlineQuery):
    time_st = time()
    rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest() + rand_str
    user_db = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user_db.insert_user()
    lang = await user_db.get_language()

    if await user_db.check_subscription():
        query_len = len(inline_query.query)

        if query_len == 0:
            await StartWithMarker(language=lang).send_inline_tip(inline_query, result_id)

        elif query_len >= TELEGRAM_CHAR_LIMIT:
            await TooLongQuery(language=lang).send_inline_tip(inline_query, result_id)

        else:
            query_t = Query(language=lang, text=inline_query.query, from_user=inline_query.from_user,
                            repeat_question=True)
            mistake = query_t.divide_query(query_t.get_markers_list())

            if not mistake:

                if ends_with_marker(inline_query.query):
                    try:
                        topic_id = await user_db.get_current_topic_id()
                        query_db = QueryDb(query_tb)
                        prev_queries_db = await query_db.get_previous_queries(topic_id=topic_id)
                        query_t.prev_messages.add_previous_queries(prev_queries_db)

                        answers = await query_t.answer_sub_queries()
                        query_t.answer = query_t.answer.format(*answers)
                        answers = [
                            InlineQueryResultArticle(
                                id=result_id,
                                title=query_t.answer,
                                input_message_content=InputTextMessageContent(message_text=query_t.answer,
                                                                              parse_mode='HTML'),
                                thumb_url="https://cdn-icons-png.flaticon.com/128/463/463574.png"
                            )
                        ]
                        await inline_query.answer(
                            results=answers,
                            cache_time=1
                        )
                        time_f = time()
                        print(time_f - time_st)
                        print(result_id)

                        for sub_query in query_t.sub_queries:
                            await query_db.insert_query(result_id=result_id,
                                                        query=sub_query.text,
                                                        answer=sub_query.answer,
                                                        topic_id=topic_id,
                                                        user_id=user_db.user_id)
                    except Exception as ex:
                        print(datetime.datetime.now(), ex, sep="   inline  ")
                        await MsgAnswerMistake(language=lang).send_inline_tip(inline_query, result_id)
                else:

                    if query_len <= 20:
                        await EndWithSign(language=lang).send_inline_tip(inline_query, result_id)

                    elif random.random() < END_TIP_PROBABILITY:
                        await EndWithSign(language=lang).send_inline_tip(inline_query, result_id)

                    else:
                        rand_tip = InfoTip(language=lang).get_random_tip()
                        await rand_tip.send_inline_tip(inline_query, result_id)
            else:
                await mistake.send_inline_tip(inline_query, result_id)
    else:
        await NoSubscription(language=lang).send_inline_tip(inline_query, result_id)


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo, lambda inline_query: True)
