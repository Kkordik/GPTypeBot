from texts import texts, guide_texts
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from classes.Guide import Guide, GuidePage
from classes.MainClasses import Topic
from typing import List
from classes.Invoice import MyInvoice


def start_keyboard(lang: str):
    first_guide_page = GuidePage(language=lang, text_name=Guide.texts_names_l[0])
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["guide_but"],
                                      callback_data="guide-" + first_guide_page.text_name))
    keyboard.add(InlineKeyboardButton(texts[lang]["context_but"], callback_data="context"))
    keyboard.add(InlineKeyboardButton(texts[lang]["premium_but"], callback_data="premium"))
    keyboard.add(InlineKeyboardButton(texts[lang]["start_inline_use_but"], switch_inline_query=""))
    return keyboard


def message_tip_keyboard(guide_page_name: str, bot_but_text: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=bot_but_text, callback_data=f"guide-{guide_page_name}"))
    return keyboard


def topics_keyboard(topics: List[Topic], lang: str, chosen_topic_id: int):
    keyboard = InlineKeyboardMarkup()

    if chosen_topic_id == 0:
        keyboard.add(InlineKeyboardButton(text="📌 " + texts[lang]["no_topic"], callback_data="topic-0"))
    else:
        keyboard.add(InlineKeyboardButton(text=texts[lang]["no_topic"], callback_data="topic-0"))

    for topic in topics:
        if topic.topic_id == chosen_topic_id:
            keyboard.add(InlineKeyboardButton(
                text=texts[lang]["topic_but_chosen"].format(topic.topic_title, topic.msg_amount),
                callback_data=f"topic-{topic.topic_id}")
            )
        else:
            keyboard.add(InlineKeyboardButton(
                text=texts[lang]["topic_but"].format(topic.topic_title, topic.msg_amount),
                callback_data=f"topic-{topic.topic_id}")
            )

    keyboard.add(InlineKeyboardButton(text=texts[lang]["create_topic_but"], callback_data="create_topic"))

    return keyboard


def buy_subs_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["buy_subs_but"], callback_data="premium"))
    return keyboard


def cancel_state_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["cancel_but"], callback_data="cancel-state"))
    return keyboard


def ask_return_inline(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["return_inline_but"], callback_data="return_inline"))
    return keyboard


def return_inline_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["return_approve_but"], switch_inline_query=""))
    return keyboard


def payment_method_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    for invoice_class in MyInvoice.__subclasses__():
        keyboard.add(InlineKeyboardButton(text=texts[lang][invoice_class.button_name],
                                          callback_data=invoice_class().get_callback_data()))
    return keyboard


async def payment_currencies_keyboard(lang: str, chosen_method_cl: MyInvoice):
    keyboard = InlineKeyboardMarkup()
    for currency in await chosen_method_cl.get_currencies_list():
        keyboard.add(InlineKeyboardButton(text=currency,
                                          callback_data=await chosen_method_cl.get_currency_callback_data(currency)))
    keyboard.add(InlineKeyboardButton(text=texts[lang]["back_payment_but"], callback_data="premium"))
    return keyboard


def after_pay_keyboard(lang: str):
    first_guide_page = GuidePage(language=lang, text_name=Guide.texts_names_l[0])
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["guide_but"],
                                      callback_data="guide-" + first_guide_page.text_name))
    keyboard.add(InlineKeyboardButton(texts[lang]["context_but"], callback_data="context"))
    keyboard.add(InlineKeyboardButton(texts[lang]["start_inline_use_but"], switch_inline_query=""))
    return keyboard
