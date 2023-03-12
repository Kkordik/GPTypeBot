from aiogram import types
from run_bot import bot
from classes.Tables import Table, UsersTable
from config import BASIC_LANGUAGE
from texts import texts


class MainClassBase:
    def __init__(self, table, row_id: int = None):
        self.table: Table = table
        self.row_id = row_id


class User(MainClassBase):
    def __init__(self, table: UsersTable, user_id, user: types.User = None, row_id: int = None,
                 language: str = BASIC_LANGUAGE, date_time: str = None, subscriber: bool = False):
        super().__init__(table, row_id)

        self.user: types.User = user
        self.user_id: int = int(user_id)
        self.language = language
        self.date_time: str = date_time
        self.subscriber: bool = subscriber

    async def __get_row_id(self):
        res = await self.table.select_vals(user_id=self.user_id)
        self.row_id = res[0]["id"]
        return self.row_id

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
