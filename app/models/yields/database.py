import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class DB_Model():
    """Model for interacting with database"""
    def __init__(self) -> None:
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = 'yields'

    def __connect__(self) -> None:
        self.connect = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pword,
            database=self.db,
        )
        self.cur = self.connect.cursor()

    def __disconnect__(self) -> None:
        self.connect.close()

    def fetch(self, query: list, dates: list = []) -> tuple:
        """Method to fetch data for a given query and/or dates from database"""
        self.__connect__()
        if True in query:
            if len(dates) > 1:
                self.cur.execute(query[0], (tuple(i for i in dates), ))
            else:
                self.cur.execute(query[0], (dates[0], ))
        else:
            self.cur.execute(query[0])

        result = self.cur.fetchall()
        print(result)
        self.__disconnect__()
        return result

    def table_nuke(self, table: str) -> None:
        self.__connect__()
        query = f"DROP TABLE {table}"
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def execute(self, query: str) -> None:
        self.__connect__()
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def executemany(self, query: str, data: list) -> None:
        self.__connect__()
        self.cur.executemany(query, data)
        self.connect.commit()
        self.__disconnect__()

    def create_table(self, query: str) -> None:
        self.__connect__()
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()
