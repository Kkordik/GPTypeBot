from aiogram import types
from run_bot import bot
from classes.Tables import Table, UsersTable, QueryTable
from config import BASIC_LANGUAGE
from texts import texts


class User:
    def __init__(self, table: UsersTable, user_id, user: types.User = None,
                 language: str = BASIC_LANGUAGE, date_time: str = None, subscriber: bool = False):
        self.table: Table = table
        self.user: types.User = user
        self.user_id: int = int(user_id)
        self.language = language
        self.date_time: str = date_time
        self.subscriber: bool = subscriber

    async def get_language(self, user: types.User = None):
        if user:
            self.user = user

        if self.user:
            language = self.user.language_code
        else:
            self.user = await bot.get_chat(self.user_id)
            language = self.user.language_code

        if language in texts:
            self.language = language
        else:
            self.language = BASIC_LANGUAGE

        return self.language

    async def insert_user(self, user_id=None):
        if user_id:
            self.user_id = int(user_id)
        return await self.table.insert_vals(user_id=int(self.user_id), date_time=['now()'])

    async def check_subscription(self) -> bool:
        res = await self.table.select_vals(user_id=self.user_id)
        if res[0]["subscriber"] == 0:
            self.subscriber = False
        else:
            self.subscriber = True
        return self.subscriber


class QueryDb:
    def __init__(self, table: QueryTable, result_id: str = None, query: str = None, answer: str = None,
                 sent: bool = False):
        self.table: Table = table
        self.result_id: str = result_id
        self.query: str = query
        self.answer: str = answer
        self.sent: bool = sent

    async def insert_query(self, result_id: str = None, query: str = None, answer: str = None):
        self.result_id: str = result_id or self.result_id
        self.query: str = query or self.result_id
        self.answer: str = answer or self.result_id

        return await self.table.insert_vals(result_id=result_id, query=query, answer=answer)

    async def set_as_sent(self, result_id: str = None):
        self.result_id: str = result_id or self.result_id
        return await self.table.update_val(where={"result_id": result_id}, sent=1)
