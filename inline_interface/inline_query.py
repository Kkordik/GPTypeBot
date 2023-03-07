from aiogram import Dispatcher
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import hashlib
from classes.Query import Query
from texts import texts, facts
from classes.MainClasses import User
from database.run_db import user_tb
from classes.Markers import ends_with_marker


async def answer_fact_inline_query(inline_query: InlineQuery, result_id: str, fact_name: str, lang: str, *kwargs):
    text = facts[lang][fact_name]["title"].format(*kwargs)

    answers = [
        InlineQueryResultArticle(
            id=result_id,
            title=text,
            input_message_content=InputTextMessageContent(message_text=texts[lang]["share"],
                                                          parse_mode='HTML'),
            thumb_url=facts[lang][fact_name]["photo"],
        )
    ]
    await inline_query.answer(
        results=answers,
        cache_time=1,
        switch_pm_text=texts[lang]["see_more_but"],
        switch_pm_parameter=fact_name
    )


async def inline_echo(inline_query: InlineQuery):
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest()
    user_db = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user_db.insert_user()
    lang = await user_db.get_language()

    if len(inline_query.query) > 255:
        await answer_fact_inline_query(inline_query, result_id, "too_long_query", lang)
        return

    query_t = Query(text=inline_query.query, inline_query=inline_query)
    mistake = query_t.divide_query(query_t.get_markers_list())

    if not mistake:
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
        await answer_fact_inline_query(inline_query, result_id, mistake.text_name, lang, mistake.marker.marker)


async def use_end_signs(inline_query: InlineQuery):
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest()

    user_db = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user_db.insert_user()
    lang = await user_db.get_language()
    query_len = len(inline_query.query)

    if query_len == 0:
        await answer_fact_inline_query(inline_query, result_id, "start_with_marker", lang)
    elif query_len > 255:
        await answer_fact_inline_query(inline_query, result_id, "too_long_query", lang)
    else:
        await answer_fact_inline_query(inline_query, result_id, "end_with_sign", lang)


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo, lambda inline_query: ends_with_marker(inline_query.query))
    dp.register_inline_handler(use_end_signs, lambda inline_query: not ends_with_marker(inline_query.query))
