from aiogram import Dispatcher
from aiogram.types import ChosenInlineResult
from GPTBot.classes.MainClasses import QueryDb
from GPTBot.database.run_db import query_tb


async def inline_feedback(result: ChosenInlineResult):
    query_db = QueryDb(query_tb)
    await query_db.set_as_sent(result_id=result.result_id)
    await query_db.delete_all_unsent(user_id=result.from_user.id)


def register_inline_feedback_handler(dp: Dispatcher):
    dp.register_chosen_inline_handler(inline_feedback, lambda result: True)

