from aiogram import Dispatcher, types
from classes.MainClasses import User, Topic
from database.run_db import user_tb, topic_tb, query_tb
from run_bot import bot
from keyboards import topics_keyboard, buy_subs_keyboard
from texts import texts


async def context_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()
    if await user.check_subscription():
        current_topic = await user.get_current_topic_id()
        topics = await Topic(topic_tb).get_user_topics(user_id=user.user_id, query_tb=query_tb)
        keyboard = topics_keyboard(topics=topics, lang=user.language, chosen_topic_id=current_topic)

        await bot.send_message(call.message.chat.id,
                               text=texts[user.language]["topics_msg"],
                               reply_markup=keyboard)
    else:
        keyboard = buy_subs_keyboard(user.language)

        await bot.send_message(call.message.chat.id,
                               text=texts[user.language]["topics_not_subs"],
                               reply_markup=keyboard)
    await call.answer()


def register_context_call(dp: Dispatcher):
    dp.register_callback_query_handler(context_callback, lambda call: call.data == "context")
