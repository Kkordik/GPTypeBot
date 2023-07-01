import asyncio
from aiogram import Dispatcher, types
from GPTBot.classes.Query import Query
from GPTBot.classes.MainClasses import QueryDb, User
from GPTBot.classes.Tip import *
from GPTBot.database.run_db import user_tb, query_tb
from GPTBot.texts import texts
from GPTBot.keyboards import start_keyboard, ask_return_inline
from GPTBot.run_bot import bot
from GPTBot.classes.Tip import MsgAnswerMistake
import datetime
from GPTBot.config import QUERY_WAIT_TIME, QUERY_CHECK_INTERVAL, INTRO_FILE_ID


async def simple_start_cmd(message: types.Message):
    user_db = User(user_tb, message.from_user.id, user=message.from_user)
    await user_db.get_language()
    await user_db.insert_user()

    if message.text == "/start":
        await user_db.check_subscription()

        if user_db.subscriber:
            await bot.send_video(chat_id=message.chat.id,
                                 video=INTRO_FILE_ID,
                                 caption=texts[user_db.language]['start_text_subs'],
                                 parse_mode="HTML",
                                 reply_markup=start_keyboard(user_db.language))
        else:
            await user_db.get_trial_queries()
            await bot.send_video(chat_id=message.chat.id,
                                 video=INTRO_FILE_ID,
                                 caption=texts[user_db.language]['start_text'].format(user_db.trial_queries),
                                 parse_mode="HTML",
                                 reply_markup=start_keyboard(user_db.language))

    else:
        param_type = message.text.split(" ")[1].split("-")[0]
        param = message.text.split(" ")[1].split("-")[1]

        if param_type == "tip":
            tip_type = globals()[param]
            tip: Tip = tip_type(language=user_db.language)
            await tip.pm_button_reaction(bot=bot, chat_id=message.chat.id, user=message.from_user, user_db=user_db)

        elif param_type == "query":
            try:
                query_db = QueryDb(query_tb)
                sub_queries = await query_db.get_queries_by_res_id(result_id=param)

                orig_query_text = sub_queries[0].orig_query

                query_t = Query(
                    language=user_db.language,
                    text=orig_query_text,
                    from_user=message.from_user,
                    repeat_question=True
                )

                query_t.divide_query(query_t.get_markers_list())
                query_t.answer = query_t.answer.format(*[sub_query.answer for sub_query in sub_queries])

                await bot.send_message(
                    chat_id=message.chat.id,
                    text=query_t.answer,
                    disable_web_page_preview=True,
                    reply_markup=ask_return_inline(user_db.language)
                )

                await query_db.set_as_sent(result_id=param)

            except Exception as ex:
                waiting_msg = await message.answer(text=texts[user_db.language]["getting_query_ready"])
                await MsgAnswerMistake(language=user_db.language).send_message_tip(waiting_msg)
                print(datetime.datetime.now(), ex, sep="  msg_start  ")

        elif param_type == "wait_query":

            waiting_msg = await message.answer(text=texts[user_db.language]["waiting_for_openai"])
            try:
                query_db = QueryDb(query_tb)

                sub_queries = None
                for _ in range(int(QUERY_WAIT_TIME / QUERY_CHECK_INTERVAL)):

                    sub_queries = await query_db.get_queries_by_res_id(result_id=param)

                    if not sub_queries:
                        await asyncio.sleep(QUERY_CHECK_INTERVAL)
                    else:
                        break

                if not sub_queries:
                    await MsgAnswerMistake(language=user_db.language).send_message_tip(waiting_msg)
                    return

                orig_query_text = sub_queries[0].orig_query

                query_t = Query(
                    language=user_db.language,
                    text=orig_query_text,
                    from_user=message.from_user,
                    repeat_question=True
                )

                query_t.divide_query(query_t.get_markers_list())
                query_t.answer = query_t.answer.format(*[sub_query.answer for sub_query in sub_queries])

                await waiting_msg.delete()
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=query_t.answer,
                    disable_web_page_preview=True,
                    reply_markup=ask_return_inline(user_db.language)
                )

                await query_db.set_as_sent(result_id=param)

            except Exception as ex:
                await MsgAnswerMistake(language=user_db.language).send_message_tip(waiting_msg)
                print(datetime.datetime.now(), ex, sep="  msg_start wait ")


def register_main_start_cmd(dp: Dispatcher):
    dp.register_message_handler(simple_start_cmd, commands=["start"])
