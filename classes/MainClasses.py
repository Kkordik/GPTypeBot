from aiogram import types
from run_bot import bot
from classes.Table import NotFormatedValue
from classes.BotTables import Table, UsersTable, QueryTable, TopicTable, PaymentTable
from config import BASIC_LANGUAGE
from texts import texts


class User:
    def __init__(self, table: UsersTable, user_id, user: types.User = None,
                 language: str = BASIC_LANGUAGE, date_time: str = None, subscriber: bool = False,
                 current_topic_id: int = None, trial_queries: int = None):
        self.table: Table = table
        self.user: types.User = user
        self.user_id: int = int(user_id)
        self.language = language
        self.date_time: str = date_time
        self.subscriber: bool = subscriber
        self.current_topic_id: int = current_topic_id
        self.trial_queries: int = trial_queries

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
        return await self.table.insert_vals(user_id=int(self.user_id), date_time=NotFormatedValue('now()'))

    async def check_subscription(self) -> bool:
        res = await self.table.select_vals(user_id=self.user_id)
        if res[0]["subscriber"] == 0:
            self.subscriber = False
        else:
            self.subscriber = True
        return self.subscriber

    async def get_trial_queries(self) -> int:
        res = await self.table.select_vals(user_id=self.user_id)
        self.trial_queries = res[0]["trial_queries"] if not None else 0
        return self.trial_queries

    async def charge_one_trial_query(self, prev_trial_amount: int = None):
        if prev_trial_amount:
            self.trial_queries = prev_trial_amount
        elif self.trial_queries is None:
            raise Exception("Not specified old trial queries amount")

        self.trial_queries -= 1
        return await self.table.update_val(where={"user_id": self.user_id}, trial_queries=self.trial_queries)

    async def get_current_topic_id(self):
        res = await self.table.select_vals(user_id=self.user_id)
        return res[0]["current_topic"]

    async def set_new_topic(self, new_topic_id):
        return await self.table.update_val(where={"user_id": self.user_id}, current_topic=new_topic_id)

    async def make_subscriber(self):
        self.subscriber = 1
        return await self.table.update_val(where={"user_id": self.user_id}, subscriber=self.subscriber)


class QueryDb:
    def __init__(self, table: QueryTable, row_id: int = None, result_id: str = None, subquery_id: int = None,
                 orig_query: str = None, query: str = None, answer: str = None, sent: int = 0,
                 topic_id=None, user_id: int = None, date_time: str = None):
        self.table: QueryTable = table
        self.row_id: int = row_id
        self.result_id: str = result_id
        self.subquery_id: int = subquery_id
        self.orig_query: str = orig_query
        self.query: str = query
        self.answer: str = answer
        self.sent: int = sent
        self.topic_id: int = topic_id
        self.user_id: int = user_id
        self.date_time: str = date_time

    async def insert_query(self, result_id: str = None, subquery_id: int = None, orig_query: str = None,
                           query: str = None, answer: str = None, topic_id=None,
                           user_id: int = None):
        self.result_id: str = result_id or self.result_id
        self.subquery_id: int = subquery_id or self.subquery_id
        self.orig_query: str = orig_query or self.orig_query
        self.query: str = query or self.result_id
        self.answer: str = answer or self.result_id
        self.topic_id: int = topic_id
        self.user_id: int = user_id or self.user_id
        return await self.table.insert_vals(
            result_id=self.result_id,
            subquery_id=self.subquery_id,
            orig_query=self.orig_query,
            query=self.query,
            answer=self.answer,
            topic_id=self.topic_id,
            user_id=self.user_id,
        )

    async def get_queries_by_res_id(self, result_id: str = None) -> list:
        self.result_id: str = result_id or self.result_id
        sel_results = await self.table.select_vals(result_id=result_id, ending_text="ORDER BY subquery_id")
        results = []

        for res in sel_results:
            results.append(QueryDb(self.table,
                                   row_id=res["id"],
                                   result_id=res["result_id"],
                                   subquery_id=res["subquery_id"],
                                   orig_query=res["orig_query"],
                                   query=res["query"],
                                   answer=res["answer"],
                                   topic_id=res["topic_id"],
                                   sent=1))
        return results

    async def set_as_sent(self, result_id: str):
        self.result_id: str = result_id or self.result_id
        return await self.table.update_val(where={"result_id": self.result_id}, sent=1)

    async def delete_all_unsent(self, user_id):
        self.user_id = int(user_id)
        return await self.table.delete_line(sent=0, user_id=self.user_id)

    async def get_previous_queries(self, topic_id) -> list:
        """Returns list sorted in descending order"""
        if topic_id == 0:
            return []

        sel_results = await self.table.select_vals(topic_id=topic_id,
                                                   sent=1, ending_text="ORDER BY id DESC")
        results = []

        for res in sel_results:
            results.append(QueryDb(self.table,
                                   row_id=res["id"],
                                   result_id=res["result_id"],
                                   subquery_id=res["subquery_id"],
                                   orig_query=res["orig_query"],
                                   query=res["query"],
                                   answer=res["answer"],
                                   topic_id=topic_id,
                                   sent=1))
        return results

    async def count_messages(self, topic_id: int):
        self.topic_id = topic_id
        result = await self.table.db.execute_db(
            command="SELECT COUNT(*) FROM {} WHERE topic_id=%s".format(self.table.get_table_name()),
            values=[self.topic_id]
        )
        return result[0][0]


class Topic:
    def __init__(self, table: TopicTable, topic_id=None, user_id=None, topic_title: str = None, msg_amount: int = None):
        self.table: TopicTable = table
        self.topic_id: int = topic_id
        self.user_id: int = user_id
        self.topic_title: str = topic_title
        self.msg_amount: int = msg_amount

    async def get_topic(self):
        result = await self.table.select_vals(topic_id=self.topic_id)
        self.topic_title = result[0]["topic_title"]
        self.user_id = result[0]["user_id"]
        return self

    async def get_user_topics(self, user_id, query_tb):
        self.user_id = user_id
        res_topics = await self.table.select_vals(user_id=self.user_id)

        results = []
        for res in res_topics:
            topic = Topic(
                self.table,
                topic_id=res["topic_id"],
                user_id=res["user_id"],
                topic_title=res["topic_title"],
            )
            topic.msg_amount = await QueryDb(query_tb).count_messages(res["topic_id"])
            results.append(topic)
        return results

    async def create_topic(self, topic_title: str, user_id):
        self.topic_title = topic_title
        self.user_id = user_id
        await self.table.insert_vals(topic_title=self.topic_title, user_id=self.user_id)
        return self


class Payment:
    def __init__(self, table: PaymentTable, payment_id: int = None, user_id=None, date_time: str = None,
                 currency: str = None, payment_method: str = None, amount: float = None,
                 amount_usd: float = None, parameter: str = None):
        self.table: Table = table
        self.payment_id = payment_id
        self.user_id = user_id
        self.date_time = date_time
        self.currency = currency
        self.payment_method = payment_method
        self.amount = amount
        self.amount_usd = amount_usd
        self.parameter = parameter

    async def add_payment(self, user_id, currency: str, payment_method: str, amount: float, amount_usd: float,
                          parameter=None):
        self.user_id = user_id
        self.currency = currency
        self.payment_method = payment_method
        self.amount = amount
        self.amount_usd = amount_usd
        self.parameter = parameter

        await self.table.insert_vals(
            user_id=self.user_id,
            currency=self.currency,
            payment_method=self.payment_method,
            amount=self.amount,
            amount_usd=self.amount_usd,
            parameter=self.parameter
        )
        return self
