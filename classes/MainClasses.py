from aiogram import types
from run_bot import bot
from classes.Tables import Table, UsersTable, QueryTable
from config import BASIC_LANGUAGE
from texts import texts


class User:
    def __init__(self, table: UsersTable, user_id, user: types.User = None,
                 language: str = BASIC_LANGUAGE, date_time: str = None, subscriber: bool = False,
                 current_topic_id: int = None):
        self.table: Table = table
        self.user: types.User = user
        self.user_id: int = int(user_id)
        self.language = language
        self.date_time: str = date_time
        self.subscriber: bool = subscriber
        self.current_topic_id: int = current_topic_id

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

    async def get_current_topic_id(self):
        res = await self.table.select_vals(user_id=self.user_id)
        return res[0]["current_topic"]


class QueryDb:
    def __init__(self, table: QueryTable, result_id: str = None, query: str = None, answer: str = None,
                 sent: bool = False, topic_id=None, user_id: int = None):
        self.table: Table = table
        self.result_id: str = result_id
        self.query: str = query
        self.answer: str = answer
        self.sent: bool = sent
        self.topic_id: int = topic_id
        self.user_id: int = user_id

    async def insert_query(self, result_id: str = None, query: str = None, answer: str = None, topic_id=None,
                           user_id: int = None):
        self.result_id: str = result_id or self.result_id
        self.query: str = query or self.result_id
        self.answer: str = answer or self.result_id
        self.topic_id: str = topic_id or self.topic_id
        self.user_id: int = user_id or self.user_id
        return await self.table.insert_vals(result_id=self.result_id, query=self.query,
                                            answer=self.answer, topic_id=self.topic_id, user_id=self.user_id)

    async def set_as_sent(self, result_id: str):
        self.result_id: str = result_id or self.result_id
        return await self.table.update_val(where={"result_id": self.result_id}, sent=1)

    async def delete_all_unsent(self, user_id):
        self.user_id = int(user_id)
        return await self.table.delete_line(sent=0, user_id=self.user_id)

    async def get_previous_queries(self, topic_id) -> list:
        sel_results = await self.table.select_vals(topic_id=topic_id, sent=1)
        results = []
        for res in sel_results:
            results.append(QueryDb(self.table,
                                   result_id=res["result_id"],
                                   query=res["query"],
                                   answer=res["answer"],
                                   topic_id=topic_id,
                                   sent=1))
        return results


class Topic:
    def __init__(self, table: UsersTable, topic_id, user_id=None, topic_title: str = None):
        self.table: Table = table
        self.topic_id: int = int(topic_id)
        self.user_id: int = int(user_id)
        self.topic_title: str = topic_title

    async def get_topic(self):
        result = await self.table.select_vals(topic_id=self.topic_id)
        self.topic_title = result[0]["topic_title"]
        self.user_id = result[0]["user_id"]
        return self
