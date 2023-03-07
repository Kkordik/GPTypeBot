from texts import guide_texts
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Guide:
    texts_names_l = list(guide_texts["en"].keys())
    texts_names_d = dict((k, i) for i, k in enumerate(guide_texts["en"].keys()))
    length = len(texts_names_l) - 1


class GuidePage(Guide):
    video: str
    text_name: str

    def __init__(self, language: str, text_name: str):
        self.lang = language
        self.text_name = text_name
        self.text = guide_texts[self.lang][self.text_name]
        self.id = self.texts_names_d[self.text_name]

    def get_button(self) -> str:
        return guide_texts[self.lang][self.text_name]["button"]

    def create_keyboard(self):
        keyboard = InlineKeyboardMarkup()
        if self.id == 0:
            right_page = GuidePage(language=self.lang, text_name=self.texts_names_l[self.id + 1])
            keyboard.add(InlineKeyboardButton(text=right_page.text["button"] + " ➡",
                                              callback_data="guide." + right_page.text_name))
        elif self.id == self.length:
            left_page = GuidePage(language=self.lang, text_name=self.texts_names_l[self.id - 1])
            keyboard.add(InlineKeyboardButton(text="⬅ " + left_page.text["button"],
                                              callback_data="guide." + left_page.text_name))
        else:
            left_page = GuidePage(language=self.lang, text_name=self.texts_names_l[self.id - 1])
            right_page = GuidePage(language=self.lang, text_name=self.texts_names_l[self.id + 1])
            keyboard.add(InlineKeyboardButton(text="⬅ " + left_page.text["button"],
                                              callback_data="guide." + left_page.text_name),
                         InlineKeyboardButton(text=right_page.text["button"] + " ➡",
                                              callback_data="guide." + right_page.text_name))

        for example in self.text["examples"]:
            keyboard.add(InlineKeyboardButton(text=example["button"],
                                              switch_inline_query_current_chat=example["query"]))

        return keyboard

    async def send_page(self, bot,  chat_id, message: Message = None):
        if message:
            await message.edit_text(text="<i><b>Guide</b></i>\n\n" + self.text["description"],
                                    reply_markup=self.create_keyboard(),
                                    parse_mode='HTML')
        else:
            await bot.send_message(chat_id, text="<i><b>Guide</b></i>\n\n" + self.text["description"],
                                   reply_markup=self.create_keyboard(),
                                   parse_mode='HTML')
