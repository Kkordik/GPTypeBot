from aiogram import Dispatcher
from run_bot import bot
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import hashlib
from classes.inline_classes import Query
from texts import texts
from classes.main_classes import User
from database.run_db import user_tb


async def inline_echo(inline_query: InlineQuery):
    # id affects both preview and content,
    # so it has to be unique for each result
    # (Unique identifier for this result, 1-64 Bytes)
    # you can set your unique id's
    # but for example i'll generate it based on text because I know, that
    # only text will be passed in this example
    text = inline_query.query or 'echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    # if len(text) <= 250:
    #     input_content = InputTextMessageContent(text)
    # else:
    #     input_content = InputTextMessageContent("More that 250")
    #
    # item = InlineQueryResultArticle(
    #     id=result_id,
    #     title=f'Result \n{input_content.message_text}',
    #     input_message_content=input_content,
    # )
    # # don't forget to set cache_time=1 for testing (default is 300s or 5m)
    # await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1, switch_pm_text="go to pm",
    #                               switch_pm_parameter=result_id)
    user = User(user_tb, user_id=inline_query.from_user.id, user=inline_query.from_user)
    await user.insert_user()
    query_t = Query(text=inline_query.query)
    mistake = query_t.divide_query(query_t.get_markers_list())
    if not mistake:
        print([query.text for query in query_t.sub_queries])
    else:
        lang = await user.get_language()
        print(texts[lang][mistake.text_name])
    await inline_query.answer(results=[InlineQueryResultArticle(id=result_id, title="answer",
                                                               input_message_content=InputTextMessageContent(message_text="fuck you"))],
                              cache_time=1)
    # After I've checked marks order I have to divide text on queries.


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo)
