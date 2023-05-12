import asyncio
from GPTypeBot.classes.BotTables import Database, UsersTable, QueryTable, TopicTable, PaymentTable
from GPTypeBot.config import HOST, USER, PASSWORD, NAME, PORT


async def run_db(_loop, host, user, password, name, port) -> Database:
    _db = Database(host, user, password, name, port)
    await _db.make_pool(_loop)
    return _db


if __name__ == "GPTypeBot.database.run_db":
    # Register database and pool
    loop = asyncio.get_event_loop()
    db: Database = loop.run_until_complete(run_db(loop, HOST, USER, PASSWORD, NAME, PORT))

    # Register main tables
    user_tb = UsersTable(db)
    query_tb = QueryTable(db)
    topic_tb = TopicTable(db)
    payment_tb = PaymentTable(db)
