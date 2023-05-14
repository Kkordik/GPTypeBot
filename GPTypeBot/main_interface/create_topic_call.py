from aiogram import Dispatcher, types
from GPTypeBot.classes.MainClasses import User, Topic
from GPTypeBot.database.run_db import user_tb, topic_tb, query_tb
from GPTypeBot.run_bot import bot
from GPTypeBot.keyboards import topics_keyboard, buy_subs_keyboard, cancel_state_keyboard
from GPTypeBot.texts import texts
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class NewTopic(StatesGroup):
    call_message_id = State()
    ask_message_id = State()
    title = State()


async def new_topic_callback(call: types.CallbackQuery):
    user = User(user_tb, call.from_user.id, user=call.from_user)
    await user.get_language()

    if await user.check_subscription():
        await NewTopic.title.set()

        keyboard = cancel_state_keyboard(user.language)
        ask_message = await bot.send_message(call.message.chat.id,
                                             text=texts[user.language]["send_topic_title"],
                                             reply_markup=keyboard)

        state: FSMContext = Dispatcher.get_current().current_state(chat=call.message.chat.id, user=call.from_user.id)
        await state.update_data(call_message_id=call.message.message_id, ask_message_id=ask_message.message_id)

    else:
        keyboard = buy_subs_keyboard(user.language)
        await call.message.edit_text(text=texts[user.language]["topics_for_subs"], reply_markup=keyboard)

    await call.answer()


async def topic_title_msg(message: types.Message, state: FSMContext):
    state_data = await state.get_data()

    await state.finish()
    await Topic(topic_tb).create_topic(topic_title=message.text, user_id=message.from_user.id)
    await message.delete()
    await bot.delete_message(chat_id=message.chat.id, message_id=state_data["ask_message_id"])
    await bot.delete_message(chat_id=message.chat.id, message_id=state_data["call_message_id"])

    user = User(user_tb, message.from_user.id, user=message.from_user)
    await user.get_language()
    if await user.check_subscription():
        current_topic = await user.get_current_topic_id()
        topics = await Topic(topic_tb).get_user_topics(user_id=user.user_id, query_tb=query_tb)
        keyboard = topics_keyboard(topics=topics, lang=user.language, chosen_topic_id=current_topic)

        await bot.send_message(message.chat.id,
                               text=texts[user.language]["topics_msg"],
                               reply_markup=keyboard)
    else:
        keyboard = buy_subs_keyboard(user.language)

        await bot.send_message(message.chat.id,
                               text=texts[user.language]["topics_not_subs"],
                               reply_markup=keyboard)


def register_new_topic_call(dp: Dispatcher):
    dp.register_callback_query_handler(new_topic_callback, lambda call: call.data == "create_topic")
    dp.register_message_handler(topic_title_msg, content_types=["text"], state=NewTopic.title)
