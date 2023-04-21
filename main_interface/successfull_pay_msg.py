import asyncio
import datetime
from aiogram import Dispatcher, types
from classes.MainClasses import User, QueryDb
from database.run_db import user_tb, query_tb
from texts import texts, facts
from keyboards import start_keyboard
from classes.Guide import GuidePage
from run_bot import bot
from time import time
from classes.Query import Query
from classes.Tip import MsgAnswerMistake, WaitAskLater
import hashlib
import random
import string
from config import USER_ROLE, BOT_ROLE, WAIT_TIME, MISTAKE_WAIT_TIME

async def message_query(message: types.Message):
    message.successful_payment


def register_message_query_cmd(dp: Dispatcher):
    dp.register_message_handler(message_query, lambda message: message.successful_payment)
