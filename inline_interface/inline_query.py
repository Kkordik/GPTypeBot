import asyncio

from aiogram import Dispatcher
from run_bot import bot
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import hashlib
from classes.Query import Query
from texts import texts, facts
from classes.MainClasses import User
from database.run_db import user_tb
from classes.Markers import ends_with_marker
import re


async def inline_echo(inline_query: InlineQuery):
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest()
    print(result_id)
    user = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user.insert_user()
    lang = await user.get_language()

    query_t = Query(text=inline_query.query)
    mistake = query_t.divide_query(query_t.get_markers_list())

    if not mistake:
        answers = [await query.answer_query() for query in query_t.sub_queries]
        query_t.answer = query_t.answer.format(*answers)
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=query_t.answer,
                input_message_content=InputTextMessageContent(message_text=query_t.answer)
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=1
        )

    else:
        text = facts[lang][mistake.text_name].format(mistake.marker.marker)

        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=text,
                input_message_content=InputTextMessageContent(message_text=text)
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=1,
            switch_pm_text=texts[lang]["see_more_but"],
            switch_pm_parameter=mistake.text_name
        )


async def use_end_signs(inline_query: InlineQuery):
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest()

    user = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user.insert_user()
    lang = await user.get_language()

    fact = "end_with_sign"
    fact_text = facts[lang][fact]

    answers = [
        InlineQueryResultArticle(
            id=result_id,
            title=fact_text,
            input_message_content=InputTextMessageContent(message_text=fact_text)
        )
    ]
    await inline_query.answer(
        results=answers,
        cache_time=1,
        switch_pm_text=texts[lang]["see_more_but"],
        switch_pm_parameter=fact
    )


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo, lambda inline_query: ends_with_marker(inline_query.query))
    dp.register_inline_handler(use_end_signs, lambda inline_query: not ends_with_marker(inline_query.query))
