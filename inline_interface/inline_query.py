from aiogram import Dispatcher
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import hashlib
from classes.Query import Query
from texts import texts, facts
from classes.MainClasses import User
from database.run_db import user_tb
from classes.Markers import ends_with_marker
from classes.Tip import *
from config import TELEGRAM_CHAR_LIMIT, END_TIP_PROBABILITY
import random
import string
from time import time


async def inline_echo(inline_query: InlineQuery):
    time_st = time()
    rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest() + rand_str
    user_db = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user_db.insert_user()
    lang = await user_db.get_language()

    if not await user_db.check_subscription():
        await NoSubscription(language=lang).send_inline_tip(inline_query, result_id)
        return

    query_len = len(inline_query.query)

    if query_len == 0:
        await StartWithMarker(language=lang).send_inline_tip(inline_query, result_id)
        return
    elif query_len >= TELEGRAM_CHAR_LIMIT:
        await TooLongQuery(language=lang).send_inline_tip(inline_query, result_id)
        return

    query_t = Query(language=lang, text=inline_query.query, from_user=inline_query.from_user)
    mistake = query_t.divide_query(query_t.get_markers_list())

    if not mistake:
        if not ends_with_marker(inline_query.query):
            if query_len <= 20:
                await EndWithSign(language=lang).send_inline_tip(inline_query, result_id)
            elif random.random() < END_TIP_PROBABILITY:
                await EndWithSign(language=lang).send_inline_tip(inline_query, result_id)
            else:
                rand_tip = InfoTip(language=lang).get_random_tip()
                await rand_tip.send_inline_tip(inline_query, result_id)
            return

        time_f = time()
        print(time_f-time_st)
        print(result_id)
        answers = await query_t.answer_sub_queries()
        query_t.answer = query_t.answer.format(*answers)
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=query_t.answer,
                input_message_content=InputTextMessageContent(message_text=query_t.answer, parse_mode='HTML'),
                thumb_url="https://cdn-icons-png.flaticon.com/128/463/463574.png"
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=1
        )

    else:
        await mistake.send_inline_tip(inline_query, result_id)


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo, lambda inline_query: True)
