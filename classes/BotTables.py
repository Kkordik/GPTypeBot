from classes.Table import Table, Database


class UsersTable(Table):
    """
    id: smallint unsigned auto_increment
    user_id: bigint
    date_time: datetime
    subscriber: boolean
    current_topic: smallint
    trial_queries: tinyint
    """
    __name = "users"
    __columns = ["user_id", "date_time", "subscriber", "current_topic", "trial_queries"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)


class QueryTable(Table):
    """
    id	smallint unsigned
    result_id	varchar(37)
    subquery_id	tinyint
    orig_query	text
    query	text
    answer	text
    sent	tinyint(1)
    topic_id	smallint
    user_id	bigint
    date_time  datetime
    """
    __name = "queries"
    __columns = ["id", "result_id", "subquery_id", "orig_query", "query", "answer", "sent", "topic_id", "user_id",
                 "date_time"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)


class TopicTable(Table):
    """
    topic_id	smallint	NO	PRI
    user_id	bigint	NO	MUL
    topic_title	tinytext	YES
    """
    __name = "topics"
    __columns = ["topic_id", "user_id", "topic_title"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)


class PaymentTable(Table):
    """
    payment_id	int unsigned
    user_id	bigint
    date_time	datetime
    currency	tinytext
    payment_method	tinytext
    amount	float
    amount_usd	float
    parameter	tinytext
    """

    __name = "payments"
    __columns = ["payment_id", "user_id", "date_time", "currency", "payment_method", "amount", "amount_usd", "parameter"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)