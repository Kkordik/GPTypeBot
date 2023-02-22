import asyncio
from database.database_classes import Database, UsersTable, TextsTable
from config import HOST, USER, PASSWORD, NAME, PORT


async def run_db(_loop, host, user, password, name, port) -> Database:
    db = Database(host, user, password, name, port)
    await db.make_pool(_loop)
    return db


if __name__ == "database.run_db":
    # Register database and pool
    loop = asyncio.get_event_loop()
    db: Database = loop.run_until_complete(run_db(loop, HOST, USER, PASSWORD, NAME, PORT))

    # Register main tables
    user_tb = UsersTable(db)
    text_tb = TextsTable(db)
