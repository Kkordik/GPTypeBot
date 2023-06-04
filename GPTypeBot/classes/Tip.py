import aiogram.types
import GPTypeBot.classes.MainClasses
from GPTypeBot.texts import facts, texts
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle, Message
from GPTypeBot.config import INFO_PHOTO, WARNING_PHOTO, MISTAKE_PHOTO, ANSWER_PHOTO, INTRO_FILE_ID
from GPTypeBot.classes.Guide import GuidePage
from GPTypeBot.classes.Markers import BeginMarker, EndMarker
from typing import Union
from random import choices
from GPTypeBot.keyboards import message_tip_keyboard, start_keyboard
from GPTypeBot.classes.MainClasses import Topic
from GPTypeBot.database.run_db import topic_tb
from GPTypeBot.main_interface.context_call import context_message


class Tip:
    photo: str
    text_name: str = None
    guide_page_name: str
    bot_but_text_name: str = "see_more_but"
    pm_parameter = "tip"

    def __init__(self, language: str):
        self.lang = language
        self.bot_but_text = texts[self.lang][self.bot_but_text_name]
        if self.text_name:
            self.text = facts[self.lang][self.text_name]
        else:
            self.text = ""

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str, user_db):
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
            cache_time=0,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter=self.pm_parameter + "-" + self.__class__.__name__
        )

    async def send_message_tip(self, message: Message):
        await message.edit_text(
            text=self.text,
            reply_markup=message_tip_keyboard(self.guide_page_name, self.bot_but_text)
        )
    
    async def pm_button_reaction(self, bot, chat_id, user: aiogram.types.User,
                                 user_db: GPTypeBot.classes.MainClasses.User):
        guide_page = GuidePage(language=self.lang, text_name=self.guide_page_name)
        await guide_page.send_page(bot=bot, chat_id=chat_id)


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


class AnswerTip(Tip):
    photo = ANSWER_PHOTO
    bot_but_text_name = "get_in_pm_but"
    pm_parameter = "query"
    text_name = "answer_text"

    def __init__(self, language: str, answer_text: str):
        super().__init__(language)
        self.answer_text: str = answer_text

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str, user_db):
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=self.text.format(self.answer_text),
                input_message_content=InputTextMessageContent(message_text=self.answer_text),
                thumb_url=self.photo,
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=0,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter=self.pm_parameter + "-" + result_id
        )


class TimeLimitTip(Tip):
    photo = INFO_PHOTO
    bot_but_text_name = "get_in_pm_but"
    pm_parameter = "wait_query"
    text_name = "query_out_of_time"

    def __init__(self, language: str):
        super().__init__(language)

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str, user_db):
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=self.text,
                input_message_content=InputTextMessageContent(message_text=texts[self.lang]["share"]),
                thumb_url=self.photo,
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=0,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter=self.pm_parameter + "-" + result_id
        )


class EndWithSign(WarningTip):
    text_name = "end_with_sign"
    guide_page_name = "guide1"


class WrongMarkerUse(MistakeTip):
    text_name = "wrong_marker_use"
    guide_page_name = "guide1"

    def __init__(self, language: str, marker: Union[BeginMarker, EndMarker] = None):
        super().__init__(language)
        self.marker = marker

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str, user_db):
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
            cache_time=0,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter=self.pm_parameter + "-" + self.__class__.__name__
        )

    async def send_message_tip(self, message: Message):
        await message.edit_text(
            text="❌" + self.text.format(self.marker.marker),
            reply_markup=message_tip_keyboard(self.guide_page_name, self.bot_but_text)
        )


class TooLongQuery(MistakeTip):
    text_name = "too_long_query"
    guide_page_name = "guide1"


class NoSubscription(MistakeTip):
    text_name = "no_subscription"
    guide_page_name = "guide1"
    bot_but_text_name = "buy_subs_but"

    async def pm_button_reaction(self, bot, chat_id, user: aiogram.types.User,
                                 user_db: GPTypeBot.classes.MainClasses.User):
        trial_queries = await user_db.get_trial_queries()
        await bot.send_video(chat_id=chat_id,
                             video=INTRO_FILE_ID,
                             caption=texts[self.lang]['start_text'].format(trial_queries),
                             parse_mode="HTML",
                             reply_markup=start_keyboard(self.lang, start_using_but=False))


class StartWithMarker(WarningTip):
    photo = INFO_PHOTO
    text_name = "start_with_marker"
    guide_page_name = "guide1"


class WaitingTime(InfoTip):
    text_name = "waiting_time"
    guide_page_name = "guide1"


class MsgAnswerMistake(MistakeTip):
    text_name = "unknown_error"
    guide_page_name = "guide1"


class CurrentTopic(InfoTip):
    text_name = "current_topic"
    guide_page_name = "guide1"

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str, user_db):
        current_topic_id = await user_db.get_current_topic_id()

        if current_topic_id == 0:
            topic_title = texts[self.lang]["no_topic"]
        else:
            current_topic = await Topic(topic_tb, topic_id=current_topic_id).get_topic()
            topic_title = current_topic.topic_title

        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=self.text.format(topic_title),
                input_message_content=InputTextMessageContent(message_text=texts[self.lang]["share"],
                                                              parse_mode='HTML'),
                thumb_url=self.photo,
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=0,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter=self.pm_parameter + "-" + self.__class__.__name__
        )

    async def pm_button_reaction(self, bot, chat_id, user: aiogram.types.User,
                                 user_db: GPTypeBot.classes.MainClasses.User):
        await context_message(user=user, chat_id=chat_id)


class WaitAskLater(MistakeTip):
    text_name = "ask_later"
    guide_page_name = "guide1"

    def __init__(self, language: str, waiting_time: int = None):
        super().__init__(language)
        self.waiting_time = waiting_time

    async def send_inline_tip(self, inline_query: InlineQuery, result_id: str, user_db):
        answers = [
            InlineQueryResultArticle(
                id=result_id,
                title=self.text.format(self.waiting_time),
                input_message_content=InputTextMessageContent(message_text=texts[self.lang]["share"],
                                                              parse_mode='HTML'),
                thumb_url=self.photo,
            )
        ]
        await inline_query.answer(
            results=answers,
            cache_time=0,
            switch_pm_text=self.bot_but_text,
            switch_pm_parameter=self.pm_parameter + "-" + self.__class__.__name__
        )

    async def send_message_tip(self, message: Message):
        await message.edit_text(
            text="❌" + self.text.format(self.waiting_time),
            reply_markup=message_tip_keyboard(self.guide_page_name, self.bot_but_text)
        )
