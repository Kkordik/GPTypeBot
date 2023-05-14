from GPTypeBot.classes.Table import Table, Database, NotFormatedValue


class ChatTable(Table):
    """
    chat_id: bigint
    sent_msgs: smallint
    """
    __name = "chats"
    __columns = ["chat_id", "sent_msgs"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)


class ChatDb:
    def __init__(self, table: ChatTable, chat_id, sent_msgs: int = None, is_parsed: bool = None):
        self.table: ChatTable = table
        self.chat_id: int = int(chat_id)
        self.sent_msgs: int = sent_msgs
        self.is_parsed: bool = is_parsed

    async def check_is_parsed(self, chat_id=None) -> bool:
        if chat_id:
            self.chat_id = chat_id
        elif not self.chat_id:
            raise Exception("No chat_id specified to get it by id")

        res = await self.table.select_vals(chat_id=self.chat_id)

        self.is_parsed = bool(res)

        return self.is_parsed

    async def add_sent(self, chat_id=None):
        if chat_id:
            self.chat_id = chat_id
        elif not self.chat_id:
            raise Exception("No chat_id specified to add_sent")

        await self.table.update_val(where={"chat_id": self.chat_id}, sent_msgs=NotFormatedValue("sent_msgs+1"))
