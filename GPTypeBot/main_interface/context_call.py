from aiogram import Dispatcher, types
from GPTypeBot.classes.MainClasses import User, Topic
from GPTypeBot.database.run_db import user_tb, topic_tb, query_tb
from GPTypeBot.run_bot import bot
from GPTypeBot.keyboards import topics_keyboard, buy_subs_keyboard
from GPTypeBot.texts import texts


async def context_message(user: types.User, chat_id, call: types.CallbackQuery = None):
    user = User(user_tb, user.id, user=user)
    await user.get_language()
    if await user.check_subscription():
        current_topic = await user.get_current_topic_id()
        topics = await Topic(topic_tb).get_user_topics(user_id=user.user_id, query_tb=query_tb)
        keyboard = topics_keyboard(topics=topics, lang=user.language, chosen_topic_id=current_topic)

        if call:
            await call.message.edit_text(text=texts[user.language]["topics_msg"],
                                         reply_markup=keyboard)
        else:
            await bot.send_message(chat_id,
                                   text=texts[user.language]["topics_msg"],
                                   reply_markup=keyboard)
    else:
        keyboard = buy_subs_keyboard(user.language)

        await bot.send_message(chat_id,
                               text=texts[user.language]["topics_not_subs"],
                               reply_markup=keyboard)


async def context_callback(call: types.CallbackQuery):
    await context_message(user=call.from_user, chat_id=call.message.chat.id, call=call)
    await call.answer()


def register_context_call(dp: Dispatcher):
    dp.register_callback_query_handler(context_callback, lambda call: call.data == "context")
