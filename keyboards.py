from texts import texts, guide_texts
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from classes.Guide import Guide, GuidePage
from classes.MainClasses import Topic
from typing import List


def start_keyboard(lang: str):
    first_guide_page = GuidePage(language=lang, text_name=Guide.texts_names_l[0])
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["guide_but"],
                                      callback_data="guide-" + first_guide_page.text_name))
    keyboard.add(InlineKeyboardButton(texts[lang]["context_but"], callback_data="context"))
    keyboard.add(InlineKeyboardButton(texts[lang]["start_use_but"], switch_inline_query=""))
    return keyboard


def message_tip_keyboard(guide_page_name: str, bot_but_text: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=bot_but_text, callback_data=f"guide-{guide_page_name}"))
    return keyboard


def topics_keyboard(topics: List[Topic], lang: str, chosen_topic_id: int):
    keyboard = InlineKeyboardMarkup()

    if chosen_topic_id == 0:
        keyboard.add(InlineKeyboardButton(text=texts[lang]["no_topic"] + " 📌", callback_data="topic-0"))
    else:
        keyboard.add(InlineKeyboardButton(text=texts[lang]["no_topic"], callback_data="topic-0"))

    for topic in topics:
        if topic.topic_id == chosen_topic_id:
            keyboard.add(InlineKeyboardButton(text=topic.topic_title + " 📌", callback_data=f"topic-{topic.topic_id}"))
        else:
            keyboard.add(InlineKeyboardButton(text=topic.topic_title, callback_data=f"topic-{topic.topic_id}"))

    keyboard.add(InlineKeyboardButton(text=texts[lang]["create_topic_but"], callback_data="create_topic"))

    return keyboard


def buy_subs_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["buy_subs_but"], callback_data="buy-subscription"))
    return keyboard


def cancel_state_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["cancel_but"], callback_data="cancel-state"))
    return keyboard
