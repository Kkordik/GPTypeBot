import asyncio

from aiogram import Dispatcher
from run_bot import bot
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import hashlib
from classes.inline_classes import Query
from texts import texts
from classes.main_classes import User
from database.run_db import user_tb
from classes.Markers import ends_with_marker
import re


async def inline_echo(inline_query: InlineQuery):
    user = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user.insert_user()
    lang = await user.get_language()
    query_t = Query(text=inline_query.query)
    mistake = query_t.divide_query(query_t.get_markers_list())
    answers = []
    if not mistake:
        text = query_t.text
        result_id: str = hashlib.md5(text.encode()).hexdigest() + "wait"
        wait_answer = [
            InlineQueryResultArticle(
                id=result_id,
                title="wait",
                input_message_content=InputTextMessageContent(message_text=texts[lang]["wait"])
            )
        ]
        print("fdvdfv")
        await inline_query.answer(results=wait_answer, cache_time=1)
        for query in query_t.sub_queries:
            text = query.text
            result_id: str = hashlib.md5(text.encode()).hexdigest()
            answers.append(InlineQueryResultArticle(
                id=result_id, title="answer", input_message_content=InputTextMessageContent(message_text=text)))
    else:
        text = texts[lang][mistake.text_name].format(mistake.marker.marker)
        result_id: str = hashlib.md5(text.encode()).hexdigest()
        answers = [InlineQueryResultArticle(id=result_id, title=text,
                                            input_message_content=InputTextMessageContent(message_text=text))]
    print(answers)
    await bot.answer_inline_query(inline_query.id, results=answers, cache_time=1)
    print("vvvf")


async def use_end_signs(inline_query: InlineQuery):
    user = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user.insert_user()
    lang = await user.get_language()
    answers = []
    text = texts[lang]["end_with_sign"]
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    answers.append(InlineQueryResultArticle(
        id=result_id, title=text, input_message_content=InputTextMessageContent(message_text=text)))

    await inline_query.answer(results=answers, cache_time=1)


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo, lambda inline_query: ends_with_marker(inline_query.query))
    dp.register_inline_handler(use_end_signs, lambda inline_query: not ends_with_marker(inline_query.query))
