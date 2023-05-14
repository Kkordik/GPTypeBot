import asyncio
from AdvertBot.Chat import ChatTable
from AdvertBot.config import HOST, USER, PASSWORD, NAME, PORT
from GPTypeBot.classes.Table import Database


async def run_db(_loop, host, user, password, name, port) -> Database:
    _db = Database(host, user, password, name, port)
    await _db.make_pool(_loop)
    return _db


if __name__ == "AdvertBot.run_db":
    # Register database and pool
    loop = asyncio.get_event_loop()
    db: Database = loop.run_until_complete(run_db(loop, HOST, USER, PASSWORD, NAME, PORT))

    # Register main tables
    chat_tb = ChatTable(db)
