import aiomysql
from aiomysql import Pool


class Database:
    def __init__(self, host: str, user: str, password: str,  name: str, pool: Pool = None, port: int = 3306):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port

        self.__name = name
        self.__pool: Pool = pool

    async def make_pool(self, loop):
        self.__pool = await aiomysql.create_pool(host=self.__host, port=self.__port, user=self.__user,
                                                 password=self.__password, db=self.__name, autocommit=False, loop=loop)
        return self.__pool

    async def execute_db(self, command: str):
        """
        Execute any given command and return fetchall

        :param command: MySQL executable command
        :return: list of fetched rows
        """
        async with self.__pool.acquire() as con:
            async with con.cursor() as cur:
                await cur.execute(command)
                res = await cur.fetchall()
            await con.commit()
        return res


class Table:
    def __init__(self, name: str, db: Database, columns: list):
        self.__name = name
        self.db = db
        self.__columns = columns

    async def execute_tb(self, command: str):
        """
        Execute any given command and return dict with values

        :param command: MySQL executable command
        :return: dict with values
        """
        res = await self.db.execute_db(command)
        results = []
        for row in res:
            results.append(dict(zip(self.__columns, row)))
        return results

    def __check_parameters(self, parameters: dict) -> dict[str: str]:
        """
        Checking if given columns in parameters dict exist in table.

        :param parameters: dict of structure {"column_name": value}
        :return: {"column_name": value}
        """
        for column in parameters.keys():
            # Checking if given columns in parameters exist in table and adding values to list
            if column in self.__columns:
                # Changing "string" to "'string'" to execute it in sql command as string
                if isinstance(parameters[column], str):
                    parameters[column] = "'{}'".format(parameters[column])
                elif isinstance(parameters[column], list):
                    parameters[column] = str(parameters[column][0])
                else:
                    parameters[column] = str(parameters[column])
            else:
                raise Exception("In table '{}' is no such column: '{}'".format(self.__name, column))
        return parameters

    async def select_vals(self, command: str = "SELECT * FROM {}", logical_expr: str = "AND", **where):
        """
        Selects all from table can be executed with WHERE using AND or other logical_expression

        :param command: MySQL executable command
        :param logical_expr: logical expression 'AND'/'OR'...
        :param where: optional parameters for WHERE expression
        :return: dict with values if they are
        """
        where = self.__check_parameters(where)

        # Create string WHERE expression
        if len(where) != 0:
            where_str = "WHERE"
            where_equations = []
            for column in where.keys():
                where_equations.append(" {}={} ".format(column, where[column]))
            where_str += logical_expr.join(where_equations)
        else:
            where_str = ""

        return await self.execute_tb("{} {}".format(command.format(self.__name), where_str))

    async def delete_line(self, command: str = "DELETE FROM {}", logical_expr: str = "AND", **where):
        """
        Deletes all from table must be executed with WHERE, you may use AND or other logical_expression

        :param command: MySQL executable command
        :param logical_expr: logical expression 'AND'/'OR'...
        :param where: optional parameters for WHERE expression
        :return: dict with values if they are
        """
        where = self.__check_parameters(where)

        # Create string WHERE expression
        if len(where) != 0:
            where_str = "WHERE"
            where_equations = []
            for column in where.keys():
                where_equations.append(" {}={} ".format(column, where[column]))
            where_str += logical_expr.join(where_equations)
        else:
            raise Exception("No where arguments given. It is impossible to delete all from table")

        return await self.execute_tb("{} {}".format(command.format(self.__name), where_str))

    async def insert_vals(self, command: str = "INSERT IGNORE INTO {}({}) VALUES ({})", **columns_vals):
        """
        Insert values in table.

        :param columns_vals: parameters for INSERT must consist new data.
        :param command: MySQL command for inserting new values
        :return: list of fetched rows if they are
        """
        if len(columns_vals) == 0:
            raise Exception("No parameters given")

        columns_vals = self.__check_parameters(columns_vals)

        unpack_values = ', '.join(columns_vals.values())
        unpack_columns = ', '.join(columns_vals.keys())
        return await self.execute_tb(command.format(self.__name, unpack_columns, unpack_values))

    async def launch_table(self,  *args, **kwargs):
        pass

    async def update_val(self, *args, **kwargs):
        pass


class UsersTable(Table):
    """
    id: smallint unsigned auto_increment
    user_id: bigint
    donation: smallint
    api_key: text
    date_time: datetime
    """
    __name = "users"
    __columns = ["id", "user_id", "donation", "api_key", "date_time"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)