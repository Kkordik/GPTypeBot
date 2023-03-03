from texts import texts
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard(lang: str):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(texts[lang]["guide_but"], callback_data="guide_but"))
    keyboard.add(InlineKeyboardButton(texts[lang]["start_use_but"], callback_data="start_use_but"))
    return keyboard
