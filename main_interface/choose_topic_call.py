import aiogram.utils.exceptions
from aiogram import Dispatcher, types
from classes.MainClasses import User, Topic
from database.run_db import user_tb, topic_tb, query_tb
from run_bot import bot
from keyboards import topics_keyboard, buy_subs_keyboard
from texts import texts


async def choose_topic_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    if await user.check_subscription():
        new_topic_id = call.data.split("-")[1]

        current_topic = await user.get_current_topic_id()
        topics = await Topic(topic_tb).get_user_topics(user_id=user.user_id, query_tb=query_tb)
        keyboard = topics_keyboard(topics=topics, lang=user.language, chosen_topic_id=new_topic_id)

        if new_topic_id != current_topic:
            await user.set_new_topic(new_topic_id=new_topic_id)
            await call.message.edit_reply_markup(reply_markup=keyboard)
        else:
            await call.answer(texts[user.language]["already_chosen"])
    else:
        keyboard = buy_subs_keyboard(user.language)

        await bot.send_message(call.message.chat.id,
                               text=texts[user.language]["topics_not_subs"],
                               reply_markup=keyboard)
    await call.answer()


def register_choose_topic_call(dp: Dispatcher):
    dp.register_callback_query_handler(choose_topic_callback, lambda call: call.data.split("-")[0] == "topic")
