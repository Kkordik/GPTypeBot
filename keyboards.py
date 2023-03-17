from texts import texts, guide_texts
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from classes.Guide import Guide, GuidePage


def start_keyboard(lang: str):
    first_guide_page = GuidePage(language=lang, text_name=Guide.texts_names_l[0])
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=texts[lang]["guide_but"],
                                      callback_data="guide-" + first_guide_page.text_name))
    keyboard.add(InlineKeyboardButton(texts[lang]["start_use_but"], switch_inline_query=""))
    return keyboard


def message_tip_keyboard(guide_page_name: str, bot_but_text: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=bot_but_text, callback_data=f"guide-{guide_page_name}"))
    return keyboard
