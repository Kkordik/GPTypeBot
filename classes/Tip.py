from texts import facts, texts
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle, Message
from random import choices
from config import INFO_PHOTO, WARNING_PHOTO, MISTAKE_PHOTO
from classes.Guide import GuidePage
from classes.Markers import BeginMarker, EndMarker
from typing import Union
from random import choices
from keyboards import message_tip_keyboard


class Tip:
    photo: str
    text_name: str = None
    guide_page_name: str
    bot_but_text_name: str = "see_more_but"

    def __init__(self, language: str):
        self.lang = language
        self.bot_but_text = texts[self.lang][self.bot_but_text_name]
        if self.text_name:
            self.text = facts[self.lang][self.text_name]
        else:
            self.text = ""

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str):
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=self.text,
                input_message_content=InputTextMessageContent(message_text=texts[self.lang]["share"],
                                                              parse_mode='HTML'),
                thumb_url=self.photo,
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=1,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter="guide-" + self.guide_page_name
        )

    async def send_message_tip(self, message: Message):
        await message.edit_text(
            text=self.text,
            reply_markup=message_tip_keyboard(self.guide_page_name, self.bot_but_text)
        )


class WarningTip(Tip):
    photo = WARNING_PHOTO


class MistakeTip(Tip):
    photo = MISTAKE_PHOTO


class InfoTip(Tip):
    photo = INFO_PHOTO

    def get_random_tip(self):
        """
        :return: object of randomly chosen type (subclass of InfoTip)
        """
        return choices(InfoTip.__subclasses__())[0](self.lang)


class EndWithSign(WarningTip):
    text_name = "end_with_sign"
    guide_page_name = "marked_query"


class WrongMarkerUse(MistakeTip):
    text_name = "wrong_marker_use"
    guide_page_name = "marked_query"

    def __init__(self, language: str, marker: Union[BeginMarker, EndMarker]):
        super().__init__(language)
        self.marker = marker

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str):
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=self.text.format(self.marker.marker),
                input_message_content=InputTextMessageContent(message_text=texts[self.lang]["share"],
                                                              parse_mode='HTML'),
                thumb_url=self.photo,
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=1,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter="guide-" + self.guide_page_name
        )

    async def send_message_tip(self, message: Message):
        await message.edit_text(
            text="❌" + self.text.format(self.marker.marker),
            reply_markup=message_tip_keyboard(self.guide_page_name, self.bot_but_text)
        )


class TooLongQuery(MistakeTip):
    text_name = "too_long_query"
    guide_page_name = "simple_query"


class NoSubscription(MistakeTip):
    text_name = "no_subscription"
    guide_page_name = "simple_query"
    bot_but_text_name = "buy_subs_but"


class StartWithMarker(WarningTip):
    photo = INFO_PHOTO
    text_name = "start_with_marker"
    guide_page_name = "simple_query"


class WaitingTime(InfoTip):
    text_name = "waiting_time"
    guide_page_name = "simple_query"


class MsgAnswerMistake(MistakeTip):
    text_name = "unknown_error"
    guide_page_name = "simple_query"