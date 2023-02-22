from typing import Union
from aiogram import types
from run_bot import bot
from database.database_classes import Table, UsersTable, TextsTable
from config import BASIC_LANGUAGE


class MainClassBase:
    def __init__(self, table, row_id: int = None):
        self.table: Table = table
        self.row_id = row_id


class User(MainClassBase):
    def __init__(self, table: UsersTable, user_id, user: types.User = None, row_id: int = None,
                 language: str = BASIC_LANGUAGE, donation: int = None, api_key: str = None):
        super().__init__(table, row_id)

        self.user: types.User = user
        self.user_id: int = int(user_id)
        self.language = language
        self.donation = donation
        self.api_key = api_key

    async def __get_row_id(self):
        self.row_id = await self.table.select_vals(user_id=self.user_id)["id"]
        return self.row_id

    async def get_language(self, user: types.User = None):
        if user:
            self.user = user
        if self.user:
            self.language = self.user.language_code
            return self.language
        elif self.user_id:
            self.user = await bot.get_chat(self.user_id)
            self.language = self.user.language_code
            return self.language

    async def insert_user(self, user_id=None):
        if user_id:
            self.user_id = int(user_id)
        return await self.table.insert_vals(user_id=int(self.user_id))


class Language(MainClassBase):
    def __init__(self, table: TextsTable, row_id: int = None, language: str = None):
        super().__init__(table, row_id)
        self.language: str = language


class Text(MainClassBase):
    def __init__(self, table: TextsTable, row_id: int = None, text_name: str = None, text: str = None,
                 language: str = None):
        super().__init__(table, row_id)

        self.text_name: str = text_name
        self.text: str = text
        self.language: str = language

    async def get_texts(self, language: str = None, text_name: str = None) -> []:
        """
        Get all texts defined by text_name and language(can be None)
        :param language:
        :param text_name:
        :return: list Text objects
        """
        if text_name:
            self.text_name = text_name

        if language:
            self.language = language

        texts = []
        if self.language:
            for text in await self.table.select_vals(language=self.language, text_name=self.text_name):
                texts.append(Text(self.table, text_name=text["text_name"], text=text["text"],
                                  language=text["language"]))
        else:
            for text in await self.table.select_vals(text_name=self.text_name):
                texts.append(Text(self.table, text_name=text["text_name"], text=text["text"],
                                  language=text["language"]))
        return texts

    async def get_const_text(self, language, text_name: str = None) -> str:
        """
        Get constant text from database.
        :param language:
        :param text_name:
        :return: str (text of first returned object from db)
        """
        res = await self.get_texts(language, text_name)
        self.text = res[0].text
        return self.text
