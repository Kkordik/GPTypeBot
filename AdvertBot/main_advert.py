import asyncio

import pyrogram.types
from pyrogram import Client
from AdvertBot.config import api_hash, api_id
import datetime
from aiogram import Dispatcher, types
from GPTypeBot.classes.MainClasses import User, QueryDb
from GPTypeBot.database.run_db import user_tb, query_tb
from GPTypeBot.texts import texts
from GPTypeBot.run_bot import bot
from time import time
from GPTypeBot.classes.Query import Query
from GPTypeBot.classes.Tip import MsgAnswerMistake, WaitAskLater
import hashlib
import random
import string
from AdvertBot.run_db import chat_tb
from AdvertBot.Chat import ChatDb

app = Client("my_account", api_id, api_hash)


@app.on_message()
async def my_handler(client: pyrogram.Client, message: pyrogram.types.Message):

    chat_db = ChatDb(table=chat_tb, chat_id=message.chat.id)

    if await chat_db.check_is_parsed():
        discussion_msg = await app.get_discussion_message(chat_id=message.chat.id, message_id=message.id)
        if not discussion_msg:
            return

        if message.text:
            text = message.text
        elif message.caption:
            text = message.caption
        else:
            return

        rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        result_id: str = hashlib.md5(text.encode()).hexdigest() + rand_str

        try:
            # Dividing query into sub-queries or if only one query - getting it as a sub-query.
            # And replacing sub-queries in answer text with {} to make possible later add answers at the same places
            size = random.choice(["short ", ""])
            query_t = Query(
                language="en",
                text=f"-s Create a {size}comment to the post use only the language of the post: {text} -q",
                short_answers=False
            )
            mistake, _ = query_t.divide_query(query_t.get_markers_list())

            # Adding previous messages to the query based on the user's current chosen topic.
            # If topic_id is 0 than no history is taken
            topic_id = 0
            query_db = QueryDb(query_tb)
            prev_queries_db = await query_db.get_previous_queries(topic_id=topic_id)
            query_t.prev_messages.add_previous_queries(prev_queries_db)

            # Receiving answers to the sub-queries
            answers = await query_t.answer_sub_queries()
            query_t.answer = query_t.answer.format(*answers)  # Replacing {} with answers in the answer text

            # Delete all unsent messages from the database (only to free the memory because
            # such messages aren't taken to the context)
            me_user = await app.get_me()
            await query_db.delete_all_unsent(user_id=me_user.id)

            # Adding sub-queries to the database and setting as sent
            for sub_query_id, sub_query in enumerate(query_t.sub_queries):
                await query_db.insert_query(
                    result_id=result_id,
                    subquery_id=sub_query_id,
                    orig_query=query_t.text,
                    query=sub_query.text,
                    answer=sub_query.answer,
                    topic_id=topic_id,
                    user_id=me_user.id
                )

        except Exception as ex:
            print(datetime.datetime.now(), ex, sep="  msg  ")

        await asyncio.sleep(random.randint(30, 900))
        results = await app.get_inline_bot_results(bot="GPTypeBot", query="get_by_id."+result_id)

        await app.send_inline_bot_result(chat_id=discussion_msg.chat.id,
                                         query_id=results.query_id,
                                         result_id=results.results[0].id,
                                         reply_to_message_id=discussion_msg.id)
        await chat_db.add_sent()


if __name__ == "__main__":
    app.run()
