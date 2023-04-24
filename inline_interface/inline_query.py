from aiogram import Dispatcher
from aiogram.types import InlineQuery
import hashlib
from classes.Query import Query
from texts import example_queries
from classes.MainClasses import User, QueryDb
from database.run_db import user_tb, query_tb
from classes.Markers import ends_with_marker
from classes.Tip import NoSubscription, StartWithMarker, TooLongQuery, MsgAnswerMistake, EndWithSign, InfoTip, AnswerTip
from config import TELEGRAM_CHAR_LIMIT, END_TIP_PROBABILITY, INLINE_DEF_TOKEN_NUM, INLINE_MAX_TOKEN_NUM
import random
import string
import datetime


async def inline_echo(inline_query: InlineQuery):
    rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    result_id: str = hashlib.md5(inline_query.query.encode()).hexdigest() + rand_str

    # Inserting user to db and getting user's language
    user_db = User(
        user_tb,
        user_id=inline_query.from_user.id,
        user=inline_query.from_user
    )
    await user_db.insert_user()
    lang = await user_db.get_language()

    try:
        is_subs = await user_db.check_subscription()
        trial_q = await user_db.get_trial_queries()
        is_example = inline_query.query in example_queries

        # Returning inline tip if the user isn't a subscriber
        if not (is_subs or trial_q > 0 or is_example):
            return await NoSubscription(language=lang).send_inline_tip(inline_query, result_id, user_db)

        # Returning mistake tips if length of query 0 or more than limit of the Telegram
        query_len = len(inline_query.query)
        if query_len == 0:
            return await StartWithMarker(language=lang).send_inline_tip(inline_query, result_id, user_db)
        elif query_len >= TELEGRAM_CHAR_LIMIT:
            return await TooLongQuery(language=lang).send_inline_tip(inline_query, result_id, user_db)

        # Dividing query into sub-queries or if only one query - getting it as a sub-query.
        # And replacing sub-queries in answer text with {} to make possible later add answers at the same places
        query_t = Query(
            language=lang,
            text=inline_query.query,
            from_user=inline_query.from_user,
            repeat_question=True
        )
        mistake, _ = query_t.divide_query(
            query_t.get_markers_list()
        )

        # Returning mistake marker if while dividing query found wrong markers usage
        if mistake:
            return await mistake.send_inline_tip(inline_query, result_id, user_db)

        # Returning some info tips if query hasn't been finished yet
        if not ends_with_marker(inline_query.query):
            if query_len <= 20:
                return await EndWithSign(language=lang).send_inline_tip(inline_query, result_id, user_db)

            elif random.random() < END_TIP_PROBABILITY:
                return await EndWithSign(language=lang).send_inline_tip(inline_query, result_id, user_db)

            else:
                rand_tip = InfoTip(language=lang).get_random_tip()
                return await rand_tip.send_inline_tip(inline_query, result_id, user_db)

        # Adding previous messages to the query based on the user's current chosen topic.
        # If topic_id is 0 than no history is taken
        topic_id = await user_db.get_current_topic_id()
        query_db = QueryDb(query_tb)
        prev_queries_db = await query_db.get_previous_queries(topic_id=topic_id)
        query_t.prev_messages.add_previous_queries(
            prev_queries_db=prev_queries_db,
            default_token_num=INLINE_DEF_TOKEN_NUM,
            max_token_num=INLINE_MAX_TOKEN_NUM
        )

        # Receiving answers on the sub-queries
        answers = await query_t.answer_sub_queries(max_token_num=INLINE_MAX_TOKEN_NUM)
        query_t.answer = query_t.answer.format(*answers)  # Replacing {} with answers in the answer text

        answer_tip = AnswerTip(language=lang, text=query_t.answer)
        await answer_tip.send_inline_tip(inline_query=inline_query, result_id=result_id, user_db=user_db)

        # Adding sub-queries to the database
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
        if not (user_db.subscriber or is_example):
            await user_db.charge_one_trial_query(prev_trial_amount=user_db.trial_queries)

    except Exception as ex:
        print(result_id, datetime.datetime.now(), ex, sep="   inline   ")
        await MsgAnswerMistake(language=lang).send_inline_tip(inline_query, result_id, user_db)


def register_inline_query_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_echo, lambda inline_query: True)
